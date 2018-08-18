
function load() {

  function detectWebGLContext () {
    var canvas = document.createElement("canvas");
    var gl = canvas.getContext("webgl")
      || canvas.getContext("experimental-webgl");
    if (gl && gl instanceof WebGLRenderingContext) {
      createLogo()
    } else {
      logodiv = document.getElementsByClassName('logo-readium')[0];
      logodiv.innerHTML = '<span class="logo">B</span>'
    }
  }
  detectWebGLContext()
}
window.onload = load


createLogo = function() {

    logodiv = document.getElementsByClassName('logo-readium')[0];

    // Camera
    var camera = new THREE.PerspectiveCamera( 75, logodiv.clientWidth / logodiv.clientHeight, 0.1, 1000 );
    camera.position.set( 0, 0, 40 );

    // Scene
    scene = new THREE.Scene();
    scene.background = new THREE.Color( 0x000000 );

    // Renderer
    container = document.createElement( 'div' );
    logodiv.appendChild( container );
    var renderer = new THREE.WebGLRenderer();
    renderer.setSize( logodiv.clientWidth, logodiv.clientHeight );
    container.appendChild( renderer.domElement );

    lightboxgeom = new THREE.BoxGeometry( 1, 1, 1 )
    lightboxmaterial = new THREE.MeshBasicMaterial({color: 0xffffff})
    lightbox = new THREE.Mesh(lightboxgeom, lightboxmaterial)
    // scene.add(lightbox)

    // Lights
    var light = new THREE.AmbientLight( 0xffffff, 0.9 )
    var pointlight = new THREE.PointLight( 0xba6f00, 1.0 , 0 )

    var lightpivot = new THREE.Group();
    scene.add(light)
    pointlight.position.set(15, 0, 0)
    lightbox.position.set(15, 0, 0)
    lightpivot.add(pointlight)
    // lightpivot.add(lightbox)
    scene.add(lightpivot)


    function initText(font) {

        var textMaterial = new THREE.MeshLambertMaterial({color: 0xaaaaaa});

        let newTextGeometry = ( text ) => {
            var textGeometry = new THREE.TextGeometry(text, {
                font: font,
                size: 40,
                height: 15
            });
            textGeometry.computeBoundingBox()
            return textGeometry
        }

        textMesh = new THREE.Mesh(newTextGeometry('B'), textMaterial);

        var centerOffset = -0.5 * ( textMesh.geometry.boundingBox.max.x - textMesh.geometry.boundingBox.min.x );
        textMesh.position.x = centerOffset;
        textMesh.position.y = -0.5 * ( textMesh.geometry.boundingBox.max.y - textMesh.geometry.boundingBox.min.y );
        textMesh.position.z = -0.5 * ( textMesh.geometry.boundingBox.max.z - textMesh.geometry.boundingBox.min.z );
        
        pivot = new THREE.Group();
        scene.add( pivot );
        pivot.add( textMesh );
    }


    var fontLoader = new THREE.FontLoader();
    fontLoader.load("/assets/fonts/gentilis_regular.typeface.json", function(font) {
        initText(font)
        animate()
    })

    function animate() {
        requestAnimationFrame( animate );
        
        renderer.render( scene, camera );
        // pivot.rotation.x += .02;
        // pivot.rotation.y -= .02;
        // pivot.rotation.z += .02;

        lightpivot.rotation.y += 0.1;
        
    }

    var last_position = {}
    document.onscroll = function() {
        if (typeof(last_position.x) != 'undefined') {
            var deltaX = last_position.x - window.scrollX, deltaY = last_position.y - window.scrollY;
            
            if ( window.scrollY == 0 ) {
                pivot.rotation.y = 0;
                pivot.rotation.x = 0;
            } else {
                pivot.rotation.y -= deltaY / 100;    
                // pivot.rotation.x += deltaX / 100;
            }
        }

        last_position = {
            x : window.scrollX,
            y : window.scrollY
        }
    }
}
