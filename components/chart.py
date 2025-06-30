import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import streamlit as st


def display(kind, df, group_col, value_col = "", aggFunc='mean', title="Chart", barmode = 'group', xAxisTitle= "", yAxisTitle = ""):
    match kind:
        case 'bar':
            bar_chart(df, group_col, value_col, title, aggFunc)
        case 'bar_count':
            bar_count(df, group_col, value_col, barmode, title, yAxisTitle)
        
        case 'histogram':
            histogram(df, group_col, title)
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

def histogram(df, x, title):
    counts, bins = np.histogram(df[x], bins=20)
    bin_centers = 0.5 * (bins[:-1] + bins[1:])

    fig = px.histogram(
        df,
        x=df[x],
        title= title,
        nbins=20,
        opacity=0.7
    )

    fig.add_trace(go.Scatter(
        x=bin_centers,
        y=counts,
        mode='lines',
        name= 'Curva',
        line=dict(color='blue', width=2),
        marker=dict(size=4)
    ))

    st.plotly_chart(fig, use_container_width = True)

