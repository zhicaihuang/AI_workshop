# coding=utf-8
# ************************************************
# *Author*        :zhicaihuang@github.com
# *Created Time*  : 2019-12-20 15:31:01
# ************************************************

# import numpy as np

# good neutral bad
observations = ["g", "n", "b"]
states = ["sunny", "rainy", "cloudy"]
init_state_prob = {"sunny": 0.4, "rainy": 0.3, "cloudy": 0.3}
transform_prob = {
    "sunny": {"sunny": 0.2, "rainy": 0.3, "cloudy": 0.3},
    "rainy": {"sunny": 0.3, "rainy": 0.5, "cloudy": 0.2},
    "cloudy": {"sunny": 0.5, "rainy": 0.3, "cloudy": 0.2},
}
emission_prob = {
    "sunny": {"g": 0.5, "b": 0.2, "n": 0.3},
    "rainy": {"g": 0.2, "b": 0.5, "n": 0.3},
    "cloudy": {"g": 0.2, "b": 0.3, "n": 0.5},
}

# two method to find the best path, result maybe diff, because using max and sort 
# the result diff in condition of the same prob.
def viterbi(observations, states, init_state_prob, transform_prob, emission_prob):
    # last state is s, because we find the best last state, in last step, it find itself.
    path = {s: [] for s in states}
    max_pro = {}
    for c_s in states:
        max_pro[c_s] = init_state_prob[c_s] * emission_prob[c_s][observations[0]]
    print(max_pro)
    print("---------------------")

    for obs_idx in range(1, len(observations)):
        prob_state = list()
        for c_s in states:
            # path[c_s].append(c_s)
            for l_s in states:
                prob = (
                    max_pro[l_s]
                    * transform_prob[l_s][c_s]
                    * emission_prob[c_s][observations[obs_idx]]
                )
                prob_state.append((prob, l_s))
            best_prob, best_last_state = max(prob_state)
            # save all path and prob for each state
            max_pro[c_s] = best_prob
            path[c_s].append(best_last_state)
        print(obs_idx)
        print(path)
        print(max_pro)
        print("-----------------------")

    # method 1, max
    prob_state = list()
    for f_s in states:
        prob_state.append((max_pro[f_s], path[f_s] + [f_s]))
    print("prob_state", prob_state)
    best_prob, best_path = max(prob_state)
    print("-----------------------")
    print('result:',best_prob, best_path)
    print("-----------------------")

    # method 2, sort
    final_prob = -1
    # f_s: final_state
    for f_s in states:
        # the best last state is what
        path[f_s].append(f_s)
        if max_pro[f_s] > final_prob:
            best_prob = max_pro[f_s]
            best_path = path[f_s]
    print('result:',best_prob, best_path)


def main():
    # observations = ["g", "n", "b"]
    observations = ["b", "n", "b", "g", "g"]
    viterbi(observations, states, init_state_prob, transform_prob, emission_prob)
    pass


if __name__ == "__main__":
    main()
