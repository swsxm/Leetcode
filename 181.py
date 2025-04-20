import pandas as pd


def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    merged = employee.merge(
        employee[["id", "salary"]],
        left_on="managerId",
        right_on="id",
        how="inner",
        suffixes=("", "_mgr"),
    )

    richer_than_mgr = merged[merged["salary"] > merged["salary_mgr"]]
    result = richer_than_mgr[["name"]].rename(columns={"name": "Employee"})  # type: ignore[arg-type]

    return result
