import kagglehub
import pandas as pd


def load_hotel_booking() -> pd.DataFrame:
    path = kagglehub.dataset_download(
        "jessemostipak/hotel-booking-demand",
        path="hotel_bookings.csv",
    )

    df = pd.read_csv(path, compression="zip")

    return (
        df.loc[df["hotel"] == "City Hotel"]
        .drop(columns="hotel")
        .reset_index(drop=True)
    )

    return df
