---
layout: post
title:  "Spatial Vector Algebra"
date:   2023-03-12 01:30:00
categories: projects
tags: projects
---

I've found spatial vector algebra pretty confusing, as commonly found in most physics engines. So I wanted to derive a few properties here for my own sanity.

Spatial vector algebra combines linear and angular parts of motions, forces, and transformations into 6D spatial vectors (see [Rigid Body Dynamics Algorithms][rbda] by Featherstone for a more comprehensive explanation). In general, spatial vectors are more compact to code and they reduce the number of floating point operations when calculating rigid body dynamics.

### Background

Featherstone uses Plücker coordinates to represent force and motion. We'll outline the basis vectors in a bit, but to start off a motion is

$$\vec{m} = \begin{bmatrix} \vec{v} \\ \vec{\omega} \end{bmatrix}$$

and a force is

$$\vec{f} = \begin{bmatrix} \vec{F} \\ \vec{\tau} \end{bmatrix}$$

A motion is comprised of a velocity $\vec{v} = [v_x \ v_y \ v_z]$ and an angular velocity $\vec{\omega} = [\omega_x \ \omega_y \ \omega_z]$. A force is comprised of a linear force $\vec{F} = [F_x \ F_y \ F_z]$ and a torque $\vec{\tau} = [\tau_x \ \tau_y \ \tau_z]$. I'm not using the same exact notation as Featherstone, but the idea is the same.

Only certain scalar products are defined in this coordinate system. Given $\bf{m} \in M^6$ and $\bf{f} \in F^6$, $\bf{m} \cdot \bf{f}$ or $\bf{f} \cdot \bf{m}$ both mean the same thing, in this case the power delivered by a force to a body in motion. $\bf{m} \cdot \bf{m}$ and $\bf{f} \cdot \bf{f}$ are not defined. $M^6$ and $F^6$ are the space of all motions and forces, which form a dual vector space (see [RBDA][rbda] for more details on dual vector spaces). We define a basis in cartesian coordinates where the 6d basis vector is comprised of the x-y-z axes plus rotations about the x-y-z axes (i.e. Plücker basis). Dot products in dual coordinates work the same way as elsewhere (i.e. $\bf{m} \cdot \bf{f} = \vec{m}^T \vec{f}$).

One nice thing about spatial vectors is that we can now define transforms in $SE(3)$ that transform both the angular and linear components of motions/forces in one go! Let's define a transformation $\bf{X}$ that operates on motions $\bf{m}$. The same transformation applied to a force $\bf{f}$ is $\bf{X^\ast} = \bf{X^{-T}}$ where the "-T" means $(X^{-1})^T$. This is because transformations must respect the inner product, $\vec{m}^T \vec{f} = (\bf{X \vec m})^T ( \bf{X^\ast \vec f})$.

So what is the transformation of say a motion vector? A rotation is simply

$$\bf{X_{rot}} = \begin{bmatrix} E & 0\\
0 & E \end{bmatrix}$$

(rotate both the angular and linear velocities by a rotation matrix $E$). A translation is

$$\bf{X_{trans}} = \begin{bmatrix} \bf{1} & 0\\
-\vec r_\times & \bf{1} \end{bmatrix}$$

, where $\vec r_\times$ is the skew symmetric matrix cross product operator:

$$\begin{bmatrix} 0 & -z & y \\
z & 0 & -x \\
-y & x & 0 \end{bmatrix}$$

When we translate a motion, the angular velocity is untouched, hence the identity in the diagonal elements of $\bf{X_{trans}}$. A linear velocity however transforms as $\vec v^{\prime} = \vec v - \vec r \times \vec \omega$ where $\vec v^{\prime}$ is the translated velocity.

A translation followed by a rotation is now:

$$\bf{X} = \begin{bmatrix} E & 0\\
0 & E \end{bmatrix}
\begin{bmatrix} \bf{1} & 0\\
-\vec r_\times & \bf{1} \end{bmatrix} =
\begin{bmatrix} E & 0\\
-E \vec r_\times & E \end{bmatrix}
$$

Now to make use of these transformations in code, Featherstone introduces operator notations in Appendix A.2 of [RBDA][rbda]. Notably, $plx(E, r)$ is a Plücker transform where we apply a translation by $r$ and then a rotation by $E$, which we just derived above. This is really convenient since we can now implement a data structure called `Transform` in code as having two attributes, a translation and rotation, rather than a 6x6 matrix. When we want to apply the transform, we can derive equations using the 6x6 spatial matrix, and then convert the 6x6 back to the $plx$ notation to write it in code.

Something very tricky just happend though! We just separated out the translation and rotation components of a transformation $\bf{X}$ into $plx$. As you may know, translations and rotations don't commute, so the order of operations is crucially important when *applying* $plx$ in code. In other words, while $plx$ is more compact compared to the 6x6 matrix, the developer needs to keep careful track of the order of operations when applying transformations.

The Rigid Body Dynamics Library ([RBDL][rbdl]) uses Featherstone's convention and implements $plx$ as well as other spatial vector algebra. One key difference compared to other physics engines like [TDS][tds] and [brax][brax], is that operations are *left-associative* in Featherstone/RBDL, and *right-associative* in TDS and brax. We'll explain associativity in the next section.

### Associativity

Left associative transforms, as seen in [RBDA][rbda], applies transforms on the left of the motion/force. If we have two transforms $X_{1} X_{2}$ applied to force/motion, first we apply $X_{2}$ to the force/motion, then we apply $X_{1}$. Right associative transforms, as seen in [TDS][tds] or [Brax][brax], apply transforms on the right: a transform $X_{1} X_{2}$ applied to a force/motion, first applies $X_{1}$ then $X_{2}$.  We'll also use $plx$ as the Plücker transform for left-associative transforms and $plxb$ as the Plücker transform for right-associative transform.

To help interpret associativity, let's take transforms $T$ and $X$. If $T$ is left-associative, we first rotate $X$ then translate. This implies that left-associative transforms are "space frame transforms", or $T$ gets us into a parent frame. If $T$ is right-associative, we translate then rotate $X$. This implies that right-associative transforms are "body frame transforms" or $T$ gets us into a child frame.

So how are $plx$ and $plxb$ now related? Notice that transforming angular velocities from a parent frame into a child frame involves rotating by the inverse of the rotation between parent and child. If $E$ is the rotation from the parent to child frame, we must transform the angular velocity by $E^T$ to get the angular velocity in the child frame. The 6x6 transform for $plxb(E, r)$ can thus be written as:

$$plxb(E, r) =
\begin{bmatrix} E^T & 0\\
-E^T \vec r_\times & E^T \end{bmatrix}
$$

Now we can derive some formulas commonly found in a few physics engines!

### Deriving Transform * Transform

Let's first derive the $plx$ operator for two combined transformations, $\textbf{X}_2 = plx(E_2, r_2)$ and $\textbf{X}_1 = plx(E_1, r_1)$. The transformation is then:

$$\bf{X}_1 \bf{X}_2 =
\begin{bmatrix} E_1 & 0\\
-E_1 \vec r_{1\times} & E_1 \end{bmatrix}
\begin{bmatrix} E_2 & 0\\
-E_2 \vec r_{2\times} & E_2 \end{bmatrix} =
\begin{bmatrix} E_1 E_2 & 0\\
-E_1 \vec r_{1\times} E_2 - E_1 E_2 r_{2\times} & E_1 E_2  \end{bmatrix}
$$

Let's simplify the lower left entry by using the identities

$$(\vec a + \vec b)_\times = \vec a_\times + \vec b_\times$$

and

$$(E \vec a)_\times = E \vec a_\times E^{-1}$$

where $(E \vec a)_\times$ is a cross product operator by the rotated $\vec a$. Now the lower left entry of $X_1 X_2$ can be written as:

$$
\begin{multline}
\begin{split}
&-E_1 \vec r_{1\times} E_2 - E_1 E_2 \vec r_{2\times}\\
&= -E_1 E_2 (E_2^T \vec r_{1\times} E_2 + \vec r_{2\times})\\
&= -E_1 E_2 ( (E_2^T \vec r_1)_\times + \vec r_{2\times})\\
&= -E_1 E_2 ( E_2^T \vec r_1 + \vec r_{2})_\times
\end{split}
\end{multline}
$$

Notice we can now re-order $\bf{X}_1 \bf{X}_2$ to get

$$\bf{X}_1 \bf{X}_2 =
\begin{bmatrix} E_1 E_2 & 0\\
0 & E_1 E_2 \end{bmatrix}
\begin{bmatrix} \bf{1} & 0\\
-(E_2^T \vec r_1)_\times - \vec r_{2\times} & \bf{1} \end{bmatrix}
$$

which is simply $plx(E_1 E_2, E_2^T r_1 + r_2)$. If you look at RBDL, this is exactly what you [see](rbdl-transform)!

Now let's do the same thing for $plxb$, where a transformation $Y$ is right-associative. $Y_1$ or $plxb(E_1, r_1)$ and $Y_2$ or $plxb(E_2, r_2)$:

$$
\bf{Y}_2 \bf{Y}_1 =
\begin{bmatrix} E_2^T & 0\\
-E_2^T \vec r_{2\times} & E_2^T \end{bmatrix}
\begin{bmatrix} E_1^T & 0\\
-E_1^T \vec r_{1\times} & E_1^T \end{bmatrix} =
\begin{bmatrix} E'_2^T E'_1^T & 0\\
-E_2^T \vec r_{2\times} E_1^T - E_2^T E_1^T r_{1\times} & E_2^T E_1^T  \end{bmatrix}
$$

Notice that we apply $Y_1$ on the right because it is right-associative. Again simplifying the lower left entry:

$$
\begin{multline}
\begin{split}
&-E_2^T \vec r_{2\times} E'_1^T - E_2^T E_1^T r_{1\times}\\
&= -E_2^T E_1^T (E_1 \vec r_{2\times} E_1^T - \vec r_{1\times})\\
&= -E_2^T E_1^T ((E_1 \vec r_2)_{\times} +  \vec r_{1\times}) \\
&= -E_1^T E_2^T (E_1 \vec r_2 +  \vec r_1)_{\times}
\end{split}
\end{multline}
$$

Re-writing $\bf{Y}_1 \bf{Y}_2$ we get

$$
\bf{Y}_1 \bf{Y}_2 =
\begin{bmatrix} E_2^T E_1^T & 0\\
-E_2^T E_1^T (E_1 \vec r_2 +  \vec r_1)_{\times} & E_2^T E_1^T  \end{bmatrix}
$$

which is just $plxb((E_2^T E_1^T)^T, \vec r_1 + E_1 \vec r_2)$ or $plxb(E_1 E_2, \vec r_1 + E_1 \vec r_2)$. This is exactly what we see in TDS [here][tds-transform], and brax [here][brax-transform].

### Transform a Motion/Force

What about transforming a motion or force? We'll finally get to apply our spatial vector algebra using the force/motion basis! Let's say we have a transform $plx(E, r)$ (let's call the transformation $\bf{X}$) applied to a motion $\vec m$:

$$
\bf{X} \vec m\ =  
\begin{bmatrix} E & 0\\
-\vec r_\times E & E \end{bmatrix}
\begin{bmatrix} \vec \omega \\
\vec v \end{bmatrix} =
\begin{bmatrix} E \vec \omega \\
E(\vec v - \vec r \times \vec \omega) \end{bmatrix}
$$

which is exactly what we find in RLBD [here][rbdl-apply-motion]. Let's do the same thing for $plxb(E, r)$ (or a transform $\bf{Y}$) applied to a motion:

$$
\bf{Y} \vec m\ =
\begin{bmatrix} E^T & 0\\
-E^T \vec r_\times & E^T \end{bmatrix}
\begin{bmatrix} \vec \omega \\
\vec v \end{bmatrix} =
\begin{bmatrix} E^T \vec \omega \\
E^T (\vec v - \vec r \times \vec \omega) \end{bmatrix}
$$

That's what we find in [TDS][tds-apply-motion] and [brax][brax-apply-motion].

Getting the inverse transformations just amounts to taking the inverse of the 6x6, and following the same derivation as above. $X^-1$ for $plx(E, r)$ is:

$$
\begin{multline}
\begin{split}
X^{-1} &= \begin{bmatrix} E & 0\\
-E \vec r_\times & E \end{bmatrix}^{-1} =
\begin{bmatrix} \bf{1} & 0\\
-\vec r_\times & \bf{1} \end{bmatrix}^{-1}
\begin{bmatrix} E & 0\\
0 & E \end{bmatrix}^{-1}\\
&= \begin{bmatrix} \bf{1} & 0\\
\vec r_\times & \bf{1} \end{bmatrix}
\begin{bmatrix} E^T & 0\\
0 & E^T \end{bmatrix} =
\begin{bmatrix} E^T & 0\\
\vec r_\times E^T & E^T \end{bmatrix}
\end{split}
\end{multline}
$$

And $plxb(E, r)$ is:

$$
Y^{-1} = \begin{bmatrix} E^T & 0\\
-E^T \vec r_\times & E^T \end{bmatrix}^{-1} =
\begin{bmatrix} E & 0\\
\vec r_\times E & E \end{bmatrix}
$$


To get transforms applied to forces, recall that the dual transform is $\bf{X^\ast} = \bf{X^{-T}}$, which we can now derive:

$$
X^{-T} =
\begin{bmatrix} E^T & -\vec r_\times E^T\\
0 & E^T \end{bmatrix}
$$

and

$$
Y^{-T} =
\begin{bmatrix} E & \vec r_\times E\\
0 & E \end{bmatrix}
$$

Now we can apply those transformations to forces to get the corresponding code. I'll leave that to the reader!

### In conclusion

First we discussed spatial vector algebra, with some motivation based on heavy usage in physics simulators. Then we derived a few operators for applying two transforms and transforming motions/forces. Maybe one day I'll extend this a bit to inertias. Hope this is helpful so far, as I couldn't find clear derivations elsewhere on the interwebs.

Please let me know if you find errors or a more intuitive explanation of associativity!

[brax]: https://github.com/google/brax
[brax-transform]: https://github.com/google/brax/blob/855fd92ef772db0220eac47e812b78187382aefe/brax/v2/base.py#L594-L598
[brax-apply-motion]: https://github.com/google/brax/blob/855fd92ef772db0220eac47e812b78187382aefe/brax/v2/base.py#L601-L606
[tds]: https://github.com/erwincoumans/tiny-differentiable-simulator
[tds-transform]: https://github.com/erwincoumans/tiny-differentiable-simulator/blob/6c00f4d917526becbaa4404907a991b4b5307f25/src/math/transform.hpp#L123-L130
[rbda]: https://link.springer.com/book/10.1007/978-1-4899-7560-7
[rbdl]: https://rbdl.github.io/dd/df9/struct_rigid_body_dynamics_1_1_math_1_1_spatial_transform.html
[rbdl-apply-motion]: https://rbdl.github.io/d4/d41/_spatial_algebra_operators_8h_source.html#l00159
[rbdl-transform]: https://rbdl.github.io/d4/d41/_spatial_algebra_operators_8h_source.html#l00306
[tds-apply-motion]: https://github.com/erwincoumans/tiny-differentiable-simulator/blob/6c00f4d917526becbaa4404907a991b4b5307f25/src/math/transform.hpp#L210-L226
