"""
Code to generate figures in post:
    http://blog.tabanpour.info/projects/2016/04/03/optimism_rl.html

>> python optimism_rl.py

"""
import random
import numpy as np
import matplotlib.pyplot as plt

random.seed(42)


def main(max_num_tasks=2000, num_arms=10, num_plays=1500):
    Q_star = np.zeros((max_num_tasks, num_arms))
    for task in range(max_num_tasks):
        Q_star[task, :] = np.random.normal(0, 1, num_arms)

    # epsilon is the probability of choosing a random arm
    eps = 0.1
    # alpha is the step-size of the update to Q
    alpha = 0.1
    # different initial values for Q_0
    optimism = [-1, .5, 1, 5, 10]

    # REALIST
    all_rewards = np.zeros((len(optimism), max_num_tasks, num_plays))
    picked_max_action = np.zeros((len(optimism), max_num_tasks, num_plays))

    # OPTIMIST
    all_rewards_opt = np.zeros((len(optimism), max_num_tasks, num_plays))
    picked_max_action_opt = np.zeros((len(optimism), max_num_tasks, num_plays))

    for eps_idx, opt in enumerate(optimism):

        qT = np.zeros(Q_star.shape)
        qN = np.zeros((max_num_tasks, num_arms))
        qT_optimistic = np.zeros(Q_star.shape) + opt
        qN_optimistic = qN.copy()

        for b in range(max_num_tasks):
            best_arm = np.argmax(Q_star[b, :])
            #Q_star_nonstationary = Q_star.copy()
            for p in range(num_plays):

                # Include non-stationarity in Q_star,
                # each arm takes a random walk, with N(0, ns_sig)
                #Q_star_nonstationary[b, :] += np.random.normal(0, .1, 10)
                #best_arm = np.argmax(Q_star_nonstationary[b, :])

                if np.random.uniform(0, 1) <= eps:
                    # pick a random arm
                    # both the optimist and realist pick the same arm
                    #  in this case
                    arm = np.random.randint(0, num_arms)
                    arm_opt = arm
                else:
                    # pick greedy arm
                    # the optimist and realist have different expecations
                    arm = np.argmax(qT[b, :])
                    arm_opt = np.argmax(qT_optimistic[b, :])

                # determine if arm selected is the best possible
                if arm == best_arm:
                    picked_max_action[eps_idx, b, p] = 1

                if arm_opt == best_arm:
                    picked_max_action_opt[eps_idx, b, p] = 1

                # Insert some noise in the reward
                noise = np.random.normal(0, 1)

                #reward = Q_star_nonstationary[b, arm] + noise
                reward = Q_star[b, arm] + noise
                all_rewards[eps_idx, b, p] = reward
                qN[b, arm] += 1
                # qT[b, arm] = qT[b, arm] + (1 / qN[b, arm]) * (reward - qT[b, arm])
                qT[b, arm] = qT[b, arm] + (alpha) * (reward - qT[b, arm])

                #reward_opt = Q_star_nonstationary[b, arm_opt] + noise
                reward_opt = Q_star[b, arm_opt] + noise
                all_rewards_opt[eps_idx, b, p] = reward_opt
                qN_optimistic[b, arm_opt] += 1
                # qT_optimistic[b, arm_opt] = qT_optimistic[b, arm_opt] + \
                #   (1 / qN_optimistic[b, arm_opt]) * (reward_opt - qT_optimistic[b, arm_opt])
                qT_optimistic[b, arm_opt] = qT_optimistic[b, arm_opt] +\
                    (alpha) * (reward_opt - qT_optimistic[b, arm_opt])

    # Avg reward vs plays
    fig, ax = plt.subplots(1, 5, figsize=(16, 4))

    for idx, opt in enumerate(optimism):
        ax[idx].plot(
            range(num_plays),
            np.mean(all_rewards[idx, :, :], axis=0),
            label='Realist')
        ax[idx].plot(
            range(num_plays),
            np.mean(all_rewards_opt[idx, :, :], axis=0),
            label='Optimist')
        ax[idx].set_title('$Q_0=$ %.2f' % opt)
        ax[idx].set_xticks(xrange(0, num_plays+1, 300))
        ax[idx].set_xlim((0, num_plays))
        if idx == 0:
            ax[idx].set_ylabel('Average Rewards', fontsize=12)
            ax[idx].set_xlabel('Plays')
        if idx != 0:
            ax[idx].get_yaxis().set_ticks([])
        if idx == len(optimism) - 1:
            plt.legend(
                loc='lower center', shadow=True,
                bbox_to_anchor=(-1.5, 0),
                ncol=2, fancybox=True
            )

    fig.suptitle(
        '''$\epsilon$-greedy rewards with $\epsilon=$ %.1f on 10-armed test-bed with 2000 games.
            Blue line is the Realist. Green line is the Optimist.''' % eps, fontsize=14, x=.5, y=0)
    plt.savefig('avg_reward')

    # Percent picked max action vs plays
    fig, ax = plt.subplots(1, 5, figsize=(16, 4))
    for idx, opt in enumerate(optimism):
        ax[idx].plot(
            range(num_plays),
            np.mean(picked_max_action[idx, :, :], axis=0),
            label='Realist')
        ax[idx].plot(
            range(num_plays),
            np.mean(picked_max_action_opt[idx, :, :], axis=0),
            label='Optimist')
        ax[idx].set_title('$Q_0=$ %.2f' % opt)
        ax[idx].set_xticks(xrange(0, num_plays+1, 300))
        ax[idx].set_xlim((0, num_plays))
        if idx == 0:
            ax[idx].set_ylabel('% Optimal Action', fontsize=12)
            ax[idx].set_xlabel('Plays')
        if idx != 0:
            ax[idx].get_yaxis().set_ticks([])
        if idx == len(optimism) - 1:
            plt.legend(
                loc='lower center', shadow=True,
                bbox_to_anchor=(-2, 0),
                ncol=2, fancybox=True)

    fig.suptitle(
        '''$\epsilon$-greedy with $\epsilon=$ %.1f on 10-armed test-bed with 2000 games.
            Blue line is the Realist. Green line is the Optimist.''' % eps, fontsize=14, x=.5, y=0)
    plt.savefig('pct_optimal_action', )


if __name__ == '__main__':
    main()
