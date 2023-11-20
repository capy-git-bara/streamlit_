import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def main():
    st.title("Peak Waiters App for Australia")

    uploaded_file = st.file_uploader("Upload your .xlsx file")

    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        df['event_dt'] = pd.to_datetime(df['event_dt'])

        selected_public_names = st.multiselect("Select Supercharger Sites", options=df['public_name'].unique())

        if selected_public_names:
            filtered_df = df[df['public_name'].isin(selected_public_names)]

            # Plotly를 사용하여 바 그래프 생성
            fig = px.bar(filtered_df, x='event_dt', y='peak_waiters', color='public_name', title="Peak Waiters for Selected Sites")
            fig.update_xaxes(title="Date", dtick="D", tickformat="%b %d, %Y")
            fig.update_yaxes(title="Peak Waiters")

            # y = 10인 빨간색 점선 추가
            fig.add_trace(go.Scatter(x=filtered_df['event_dt'], y=[10]*len(filtered_df), mode='lines', name='Threshold', line=dict(color='red', dash='dot')))

            st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
