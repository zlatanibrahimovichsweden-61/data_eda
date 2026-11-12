import plotly.express as px
import plotly.io as pio

pio.templates.default = "plotly_white"
px.defaults.color_discrete_sequence = ["#0F766E"]


def rasma(data):
        fig = px.histogram(data, x="family_size", nbins=11, labels={"family_size": "Family size (incl. the passenger)"},
                   title="How big were the families on board?")
        fig.update_layout(bargap=0.1, yaxis_title="Passengers")
        return fig


def rasma_pie(data,COLORS):
            outcome = data["survival"].value_counts().reset_index()

            fig2 = px.pie(outcome, names="survival", values="count", hole=0.5, color="survival",
                    color_discrete_map=COLORS, title="Died vs survived")
            return fig2


def rasma_bar(data, ORDERS):
            rate = (data.groupby("age_group", observed=False)["survived"].mean().reset_index())
            fig3 = px.bar(rate, x="age_group", y="survived", text_auto=".0%",
                          category_orders={"age_group": ORDERS["age_group"]},
                          labels={"age_group": "Age group", "survived": "Survival rate"},
                          title="Survival rate by age group")
            fig3.update_layout(yaxis_tickformat=".0%")
            return fig3