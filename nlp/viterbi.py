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


def viterbi(observations, states, init_state_prob, transform_prob, emission_prob):
    # first state is s, seem as key.
    path = {s: [] for s in states}
    max_pro = {}
    for c_s in states:
        max_pro[c_s] = init_state_prob[c_s] * emission_prob[c_s][observations[0]]

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
        max_pro[c_s] = best_prob
        path[c_s].append(best_last_state)

    final_prob = -1
    # f_s: final_state
    for f_s in states:
        path[f_s].append(f_s)
        if max_pro[f_s] > final_prob:
            best_prob = max_pro[f_s]
            best_path = path[f_s]
    print(best_prob, best_path)


def main():
    # observations = ["g", "n", "b"]
    observations = ["b", "n", "b", "g"]
    viterbi(observations, states, init_state_prob, transform_prob, emission_prob)
    pass


if __name__ == "__main__":
    main()
