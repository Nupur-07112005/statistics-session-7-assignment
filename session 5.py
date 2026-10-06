def bayes_churn_probability(prior_churn, prob_email_given_churn, prob_email):
    return (prob_email_given_churn * prior_churn) / prob_email

result = bayes_churn_probability(0.15, 0.6, 0.25)

print("Probability of churn given email:", result)