import pandas as pd
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import plotly.express as px
import warnings
import plotly.io as pio

pio.templates.default = "plotly_dark"

def mobile_data_preprocessing():

    warnings.filterwarnings("ignore", category=FutureWarning)
    legend_title_font = FontProperties(weight="bold")
    financial_services_raw_df = pd.read_csv("data/mobile_service_data.csv", delimiter=",")
    column_names_map = {
    "ID": "participant_id",
    "Q1": "age",
    "Q2": "gender",
    "Q3": "marital_status",
    "Q4": "education_level",
    "Q5": "land_ownership",
    "Q6": "personal_land_ownership",
    "Q7": "mobile_phone_ownership",
    "Q8_1": "income_salaries_wages",
    "Q8_2": "income_trading_selling",
    "Q8_3": "income_services_provided",
    "Q8_4": "income_piece_work_casual_labor",
    "Q8_5": "income_rental",
    "Q8_6": "income_interest",
    "Q8_7": "income_pension",
    "Q8_8": "income_social_welfare",
    "Q8_9": "income_dependency_others",
    "Q8_10": "expenses_paid_others",
    "Q8_11": "other_income_sources",
    "Q9": "employer",
    "Q10": "main_items_sold",
    "Q11": "main_services_provided",
    "Q12": "outgoing_money_transfers",
    "Q13": "last_outgoing_money_transfer_date",
    "Q14": "incoming_money_transfers",
    "Q15": "last_incoming_money_transfer_date",
    "Q16": "frequency_mobile_money_usage_purchases",
    "Q17": "frequency_mobile_money_usage_bills",
    "Q18": "proficiency_kiswahili",
    "Q19": "proficiency_english",
    "Latitude": "latitude",
    "Longitude": "longitude",
    "mobile_money": "mobile_money_usage",
    "savings": "savings_usage",
    "borrowing": "borrowing_usage",
    "insurance": "insurance_usage",
    "mobile_money_classification": "financial_service_classification",
    }
    def replace_column_names(df, column_mappings):
        for col_name in df:
            if col_name in column_mappings:
                df.rename(columns={col_name: column_mappings[col_name]}, inplace=True)
        return df

    financial_services_df = replace_column_names(
    financial_services_raw_df, column_names_map
    )

    mapping_dict = {
    "gender": {1: "Male", 2: "Female"},
    "marital_status": {
        1: "Married",
        2: "Divorced",
        3: "Widowed",
        4: "Single/never married",
    },
    "education_level": {
        1: "No formal education",
        2: "Some primary",
        3: "Primary completed",
        4: "Post primary technical training",
        5: "Some secondary",
        6: "University or other higher education",
        7: "Don’t know",
    },
    "land_ownership": {
        1: "You personally own the land/plot where you live",
        2: "You own the land/plot together with someone else",
        3: "A household member owns the land/plot",
        4: "The land/plot is rented",
        5: "You don’t own or rent the land",
        6: "Don’t know",
    },
    "personal_land_ownership": {1: "Yes", 2: "No"},
    "mobile_phone_ownership": {1: "Yes", 2: "No"},
    "income_salaries_wages": {1: "Yes", 0: "No"},
    "income_trading_selling": {1: "Yes", 0: "No"},
    "income_services_provided": {1: "Yes", 0: "No"},
    "income_piece_work_casual_labor": {1: "Yes", 0: "No"},
    "income_rental": {1: "Yes", 0: "No"},
    "income_interest": {1: "Yes", 0: "No"},
    "income_pension": {1: "Yes", 0: "No"},
    "income_social_welfare": {1: "Yes", 0: "No"},
    "income_dependency_others": {1: "Yes", 0: "No"},
    "expenses_paid_others": {1: "Yes", 0: "No"},
    "other_income_sources": {1: "Yes", 0: "No"},
    "employer": {
        -1: "Not applicable",
        1: "Government",
        2: "Private company/business",
        3: "Individual who owns his own business",
        4: "Small scale farmer",
        5: "Commercial farmer",
        6: "Work for individual/household e.g. security guard, maid etc.",
        7: "Other",
    },
    "main_items_sold": {
        -1: "Not applicable",
        1: "Crops/produce I grow",
        2: "Products I get from livestock",
        3: "Livestock",
        4: "Fish you catch yourself/aquaculture",
        5: "Things you buy from others – agricultural products",
        6: "Things you buy from others – non-agricultural products",
        7: "Things you make (clothes, art, crafts)",
        8: "Things you collect from nature (stones, sand, thatch, herbs)",
        9: "Things you process (honey, dairy products, flour)",
        10: "Other",
    },
    "main_services_provided": {
        -1: "Not applicable",
        1: "Personal services (hairdressers, massage, etc.)",
        2: "Telecommunications/IT",
        3: "Financial services",
        4: "Transport",
        5: "Hospitality – Accommodation, restaurants, etc.",
        6: "Information/research",
        7: "Technical – mechanic, etc.",
        8: "Educational/child care",
        9: "Health services – traditional healer etc.",
        10: "Legal services",
        11: "Security",
        12: "Other, specify",
    },
    "outgoing_money_transfers": {1: "Yes", 2: "No"},
    "last_outgoing_money_transfer_date": {
        -1: "Not applicable",
        1: "Yesterday/today",
        2: "In the past 7 days",
        3: "In the past 30 days",
        4: "In the past 90 days",
        5: "More than 90 days ago but less than 6 months ago",
        6: "6 months or longer ago",
    },
    "incoming_money_transfers": {1: "Yes", 2: "No"},
    "last_incoming_money_transfer_date": {
        -1: "Not applicable",
        1: "Yesterday/today",
        2: "In the past 7 days",
        3: "In the past 30 days",
        4: "In the past 90 days",
        5: "More than 90 days ago but less than 6 months ago",
        6: "6 months or longer ago",
    },
    "frequency_mobile_money_usage_purchases": {
        -1: "Not applicable",
        1: "Never",
        2: "Daily",
        3: "Weekly",
        4: "Monthly",
        5: "Less often than monthly",
    },
    "frequency_mobile_money_usage_bills": {
        -1: "Not applicable",
        1: "Never",
        2: "Daily",
        3: "Weekly",
        4: "Monthly",
        5: "Less often than monthly",
    },
    "proficiency_kiswahili": {
        1: "Can read and write",
        2: "Can read only",
        3: "Can write only",
        4: "Can neither read nor write",
        5: "Refused to read",
    },
    "proficiency_english": {
        1: "Can read and write",
        2: "Can read only",
        3: "Can write only",
        4: "Can neither read nor write",
        5: "Refused to read",
    },
    "mobile_money_usage": {1: "Yes", 0: "No"},
    "savings_usage": {1: "Yes", 0: "No"},
    "borrowing_usage": {1: "Yes", 0: "No"},
    "insurance_usage": {1: "Yes", 0: "No"},
    "financial_service_classification": {
        0: "No mobile money and no other financial service",
        1: "No mobile money, but at least one other financial service",
        2: "Mobile money only",
        3: "Mobile money and at least one other financial service",
    },
    }

    def replace_values_with_mappings(df, mapping_dict):
        for column, mapping in mapping_dict.items():
            df[column] = df[column].replace(mapping)
        return df


    maped_financial_services_df = replace_values_with_mappings(
    financial_services_df, mapping_dict
    )

    financial_services_df["education_level"] = (
    financial_services_df["education_level"]
    .astype(str)
    .replace("8", str(financial_services_df["education_level"].mode().iloc[0]))
    )
    financial_services_df[financial_services_df["education_level"] == 8]

    abbreviated_mapping_dict = {
    "education_level": {
        "No formal education": "None",
        "Some primary": "Some Primary",
        "Primary completed": "Primary Completed",
        "Post primary technical training": "Technical Training",
        "Some secondary": "Some Secondary",
        "University or other higher education": "Higher Education",
        "Don’t know": "Unknown",
    },
    "land_ownership": {
        "You personally own the land/plot where you live": "Own Land (Live)",
        "You own the land/plot together with someone else": "Own Land (Shared)",
        "A household member owns the land/plot": "Household Owns Land",
        "The land/plot is rented": "Land Rented",
        "You don’t own or rent the land": "No Land Ownership",
        "Don’t know": "Unknown",
    },
    "employer": {
        "Not applicable": "N/A",
        "Government": "Govt",
        "Private company/business": "Private",
        "Individual who owns his own business": "Own Business",
        "Small scale farmer": "Farmer (Small)",
        "Commercial farmer": "Farmer (Commercial)",
        "Work for individual/household e.g. security guard, maid etc.": "Household Work",
        "Other": "Other",
    },
    "main_items_sold": {
        "Not applicable": "N/A",
        "Crops/produce I grow": "Crops",
        "Products I get from livestock": "Livestock Products",
        "Livestock": "Livestock",
        "Fish you catch yourself/aquaculture": "Fish/Aquaculture",
        "Things you buy from others – agricultural products": "Bought Agri Products",
        "Things you buy from others – non-agricultural products": "Bought Non-Agri Products",
        "Things you make (clothes, art, crafts)": "Handmade Products",
        "Things you collect from nature (stones, sand, thatch, herbs)": "Natural Products",
        "Things you process (honey, dairy products, flour)": "Processed Products",
        "Other": "Other",
    },
    "main_services_provided": {
        "Not applicable": "N/A",
        "Personal services (hairdressers, massage, etc.)": "Personal Services",
        "Telecommunications/IT": "Telecom/IT",
        "Financial services": "Financial Services",
        "Transport": "Transportation",
        "Hospitality – Accommodation, restaurants, etc.": "Hospitality",
        "Information/research": "Information",
        "Technical – mechanic, etc.": "Technical Services",
        "Educational/child care": "Education/Child Care",
        "Health services – traditional healer etc.": "Health Services",
        "Legal services": "Legal Services",
        "Security": "Security",
        "Other, specify": "Other",
    },
    "last_outgoing_money_transfer_date": {
        "Not applicable": "N/A",
        "Yesterday/today": "Today",
        "In the past 7 days": "Last 7 Days",
        "In the past 30 days": "Last 30 Days",
        "In the past 90 days": "Last 90 Days",
        "More than 90 days ago but less than 6 months ago": "Last 6 Months",
        "6 months or longer ago": "Over 6 Months Ago",
    },
    "last_incoming_money_transfer_date": {
        "Not applicable": "N/A",
        "Yesterday/today": "Today",
        "In the past 7 days": "Last 7 Days",
        "In the past 30 days": "Last 30 Days",
        "In the past 90 days": "Last 90 Days",
        "More than 90 days ago but less than 6 months ago": "Last 6 Months",
        "6 months or longer ago": "Over 6 Months Ago",
    },
    "frequency_mobile_money_usage_purchases": {
        "Not applicable": "N/A",
        "Never": "Never",
        "Daily": "Daily",
        "Weekly": "Weekly",
        "Monthly": "Monthly",
        "Less often than monthly": "Less than Monthly",
    },
    "frequency_mobile_money_usage_bills": {
        "Not applicable": "N/A",
        "Never": "Never",
        "Daily": "Daily",
        "Weekly": "Weekly",
        "Monthly": "Monthly",
        "Less often than monthly": "Less than Monthly",
    },
    "proficiency_kiswahili": {
        "Can read and write": "Read/Write",
        "Can read only": "Read Only",
        "Can write only": "Write Only",
        "Can neither read nor write": "Neither",
        "Refused to read": "Refused",
    },
    "proficiency_english": {
        "Can read and write": "Read/Write",
        "Can read only": "Read Only",
        "Can write only": "Write Only",
        "Can neither read nor write": "Neither",
        "Refused to read": "Refused",
    },
    "financial_service_classification": {
        "No mobile money and no other financial service": "None",
        "No mobile money, but at least one other financial service": "Other Service",
        "Mobile money only": "Mobile Money Only",
        "Mobile money and at least one other financial service": "Mobile Money & Other",
    },
    }

    abbreviated_maped_financial_services_df = replace_values_with_mappings(
    maped_financial_services_df, abbreviated_mapping_dict
    )
    maped_financial_services_df.drop_duplicates(inplace=True)

    return maped_financial_services_df

def dataset(selected_classification):
    maped_financial_services_df = mobile_data_preprocessing()
    
    if selected_classification == 'All':
        return maped_financial_services_df
    else:
        return maped_financial_services_df[maped_financial_services_df['financial_service_classification'] == selected_classification ]

def update_fig_layout(fig, title_text, xaxis_title, yaxis_title):
    fig.update_layout(
        title={
            "text": f"<b>{title_text}</b>",
            "font": {"size": 16, "family": "Arial", "color": "white"},
            "x": 0.5,
            "y": 0.95,
            "xanchor": "center",
            "yanchor": "top",
        },
        xaxis=dict(title=f"<b>{xaxis_title}</b>", color='white'),
        yaxis=dict(title=f"<b>{yaxis_title}</b>", color='white'),
        font=dict(color='white'),
        legend_title_text="Financial Services Access",
        legend_title_font=dict(size=12, color='white'),
        legend=dict(
            orientation="h",  # Horizontal orientation
            title_font=dict(size=12, color='white'),
            font=dict(size=8, color='white'),  # Smaller font size
            yanchor="bottom",  # Place legend at the bottom
            y=-0.2,  # Adjust vertical position
            xanchor="center",
            x=0.5,
        ),
        margin=dict(t=50, b=100, l=50, r=50),  # Increase bottom margin to accommodate the legend
        autosize=True,
        width=None,
        height=None
    )

def age_distribution_graph(maped_financial_services_df):
    df = maped_financial_services_df
    fig = px.box(
        df,
        x="financial_service_classification",
        y="age",
        color="financial_service_classification",
        hover_data=["financial_service_classification"],
    )
    update_fig_layout(fig, "Age Distribution by Financial Service Classification", "Financial Service Classification", "Age")
    return fig

def financial_service_by_age_graph(selected_classification):
    maped_financial_services_df = dataset(selected_classification)
    financial_service_by_age = (
        maped_financial_services_df.groupby(["age", "financial_service_classification"])
        .size()
        .reset_index(name="age_count")
    )

    fig = px.scatter(
        financial_service_by_age,
        x="age",
        y="age_count",
        color="financial_service_classification",
        color_discrete_sequence=px.colors.qualitative.Safe,
        size="age_count",
        title="Number of Participants at Each Age by Financial Service Classification",
        labels={"age": "Age", "age_count": "Number of Participants"},
        hover_name="financial_service_classification",
    )

    fig.update_traces(marker=dict(size=12, opacity=0.8))
    update_fig_layout(fig, "Number of Participants at Each Age by Financial Service Classification", "Age", "Number of Participants")
    return fig

def gender_vs_financial_services(selected_classification):
    maped_financial_services_df = dataset(selected_classification)
    fig = px.histogram(
        maped_financial_services_df,
        x="gender",
        color="financial_service_classification",
        barmode="stack",
        labels={"gender": "Gender", "count": "Number of Participants"},
        title="Relationship Between Gender and Access to Financial Services",
    )
    update_fig_layout(fig, "Relationship Between Gender and Access to Financial Services", "Gender", "Number of Participants")
    return fig

def marital_status_vs_financial_services(selected_classification):
    maped_financial_services_df = dataset(selected_classification)
    fig = px.histogram(
        maped_financial_services_df,
        x="marital_status",
        color="financial_service_classification",
        title="Relationship Between Marital Status and Access to Financial Services",
        labels={"marital_status": "Marital Status", "count": "Number of Participants"}
    )
    update_fig_layout(fig, "Relationship Between Marital Status and Access to Financial Services", "Marital Status", "Number of Participants")
    return fig

def personal_land_ownership_vs_financial_services(selected_classification):
    maped_financial_services_df = dataset(selected_classification)
    fig = px.histogram(
        maped_financial_services_df,
        x="personal_land_ownership",
        color="financial_service_classification",
        title="Personal Land Ownership and Access to Financial Services",
        labels={"personal_land_ownership": "Personal Land Ownership", "count": "Number of Participants"},
    )
    update_fig_layout(fig, "Personal Land Ownership and Access to Financial Services", "Personal Land Ownership", "Number of Participants")
    return fig

def main_items_sold_vs_financial_services(selected_classification):
    maped_financial_services_df = dataset(selected_classification)
    trading_selling_df = maped_financial_services_df[maped_financial_services_df["income_trading_selling"] == "Yes"]
    
    fig = px.histogram(
        trading_selling_df,
        x="main_items_sold",
        color="financial_service_classification",
        title="Main Items Sold by Traders/Sellers by Financial Service Access",
        labels={"main_items_sold": "Main Items Sold", "count": "Number of Participants"},
    )
    update_fig_layout(fig, "Main Items Sold by Traders/Sellers by Financial Service Access", "Main Items Sold", "Number of Participants")
    return fig

def employment_type_vs_financial_services(selected_classification):
    maped_financial_services_df = dataset(selected_classification)
    salary_wage_df = maped_financial_services_df[maped_financial_services_df["income_salaries_wages"] == "Yes"]
    
    fig = px.histogram(
        salary_wage_df,
        x="employer",
        color="financial_service_classification",
        title="Employment Type for Salary/Wage Earners by Financial Service Access",
        labels={"employer": "Employment Type", "count": "Number of Participants"},
    )
    update_fig_layout(fig, "Employment Type for Salary/Wage Earners by Financial Service Access", "Employment Type", "Number of Participants")
    return fig

def main_services_provided_vs_financial_services(selected_classification):
    maped_financial_services_df = dataset(selected_classification)
    services_df = maped_financial_services_df[maped_financial_services_df["income_services_provided"] == "Yes"]
    
    fig = px.histogram(
        services_df,
        x="main_services_provided",
        color="financial_service_classification",
        title="Main Services Provided by Service Providers by Financial Service Access",
        labels={"main_services_provided": "Main Services Provided", "count": "Number of Participants"},
    )
    update_fig_layout(fig, "Main Services Provided by Service Providers by Financial Service Access", "Main Services Provided", "Number of Participants")
    return fig

def land_ownership_vs_financial_services(selected_classification):
    maped_financial_services_df = dataset(selected_classification)
    
    fig = px.histogram(
        maped_financial_services_df,
        x="land_ownership",
        color="financial_service_classification",
        title="Relationship Between Land Ownership and Access Financial Services",
        labels={"land_ownership": "Land Ownership", "count": "Number of Participants"},
    )
    update_fig_layout(fig, "Relationship Between Land Ownership and Access Financial Services", "Land Ownership", "Number of Participants")
    return fig

def sources_of_income_vs_financial_services(selected_classification):
    maped_financial_services_df = dataset(selected_classification)
    
    columns_of_interests = [
        "income_salaries_wages",
        "income_trading_selling",
        "income_services_provided",
        "income_piece_work_casual_labor",
        "income_rental",
        "income_interest",
        "income_pension",
        "income_social_welfare",
        "income_dependency_others",
        "expenses_paid_others",
        "other_income_sources",
        "financial_service_classification",
    ]

    melted_df = pd.melt(
        maped_financial_services_df[columns_of_interests],
        id_vars=["financial_service_classification"],
        value_vars=columns_of_interests,
        ignore_index=True,
    )
    melted_df = melted_df[melted_df["value"] == "Yes"]
    grouped_result = (
        melted_df.groupby(["financial_service_classification", "variable", "value"])
        .size()
        .reset_index(name="count")
    )
    pivot_result = grouped_result.pivot_table(
        index=["variable", "value", "financial_service_classification"],
        values="count",
        aggfunc="sum",
        fill_value=0,
    ).reset_index()
    pivot_result["variable"] = pivot_result["variable"].apply(
        lambda word: word.replace("_", " ").title()
    )

    fig = px.histogram(
        pivot_result,
        x="variable",
        y="count",
        color="financial_service_classification",
        title="Relationship Between Sources of Income and Access to Financial Services",
        labels={"variable": "Source of Income", "count": "Number of Participants"},
    )
    update_fig_layout(fig, "Relationship Between Sources of Income and Access to Financial Services", "Source of Income", "Number of Participants")
    return fig

def financial_service_classification_map(data):
    map_fig = px.scatter_mapbox(
        data,
        lat="latitude",
        lon="longitude",
        color="financial_service_classification",
        hover_name="participant_id",
        hover_data={"latitude": False, "longitude": False},
        zoom=5,
        height=600
    )
    map_fig.update_layout(mapbox_style="open-street-map")
    update_fig_layout(map_fig, "Financial Services Classification Map", "Longitude", "Latitude")
    return map_fig
