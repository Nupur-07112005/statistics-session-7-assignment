def bayes_fraud_probability(prob_fraud, prob_alert_given_fraud,
                            prob_alert_given_normal):
    prob_normal = 1 - prob_fraud

    prob_alert = (
        prob_alert_given_fraud * prob_fraud
        + prob_alert_given_normal * prob_normal
    )

    return (prob_alert_given_fraud * prob_fraud) / prob_alert


result = bayes_fraud_probability(0.02, 0.90, 0.05)

print("Probability of fraud given alert:", result)
print("Percentage:", result * 100, "%")