import plotly.express as px
import streamlit as st

def display(kind, df, group_col, value_col, aggFunc='mean', title="Chart", barmode = 'group', yAxisTitle = " "):
    match kind:
        case 'bar':
            bar_chart(df, group_col, value_col, title, aggFunc)
        case 'bar_count':
            bar_count(df, group_col, value_col, barmode, title, yAxisTitle)
        case _:
            st.error(f"{kind} is not a valid chart type")
            raise ValueError("Invalid chart type")




def bar_chart(df, group_col, value_col, title, aggfunc):
    grouped = df.groupby(group_col)[value_col].agg(aggfunc).reset_index()
    fig = px.bar(
        grouped,
        x=group_col,
        y=value_col,
        title=title,
        color=group_col,
        text_auto=True
    )

    st.plotly_chart(fig, use_container_width=True)


def bar_count(df, x_col, hue_col, barmode, title, yAxisTitle):
    fig = px.histogram(
        df,
        title=title,
        x=x_col,
        color=hue_col,
        barmode= barmode,
        category_orders={x_col: df[x_col].value_counts().index.tolist()}
    )

    fig.update_layout(
        xaxis_title=x_col,
        yaxis_title=yAxisTitle,
        xaxis_tickangle=-45,
        bargap=0.15,
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)
