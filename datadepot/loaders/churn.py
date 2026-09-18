import kagglehub
import pandas as pd


def load_churn() -> pd.DataFrame:
    path = kagglehub.dataset_download(
        "sakshigoyal7/credit-card-customers",
        path="BankChurners.csv",
    )

    df = pd.read_csv(
        path,
        compression="zip",
    )

    df.columns = df.columns.str.lower().str.strip()

    df = df.rename(
        columns={
            "clientnum": "customer_id",
            "customer_age": "age",
            "education_level": "education",
            "marital_status": "marital",
            "income_category": "income",
            "total_relationship_count": "relationship_count",
            "months_inactive_12_mon": "months_inactive",
            "contacts_count_12_mon": "contacts_count",
            "total_revolving_bal": "revolving_balance",
            "avg_open_to_buy": "available_credit",
            "total_amt_chng_q4_q1": "ratio_amount_q4_q1",
            "total_trans_amt": "transaction_amount",
            "total_trans_ct": "transaction_count",
            "total_ct_chng_q4_q1": "ratio_count_q4_q1",
            "avg_utilization_ratio": "utilization_ratio",
            "attrition_flag": "churn",
        }
    )

    df = df.drop(
        columns=[
            "naive_bayes_classifier_attrition_flag_card_category_contacts_count_12_mon_dependent_count_education_level_months_inactive_12_mon_1",
            "naive_bayes_classifier_attrition_flag_card_category_contacts_count_12_mon_dependent_count_education_level_months_inactive_12_mon_2",
        ]
    )

    df["churn"] = df["churn"].map(
        {"Existing Customer": "no", "Attrited Customer": "yes"}
    )

    return df
