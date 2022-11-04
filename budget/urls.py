from django.urls import path

from budget.views import (ListBudgetView, CreateBudgetView, UpdateBudgetView, DeleteBudgetView)

app_name = "budget"


urlpatterns = [
    path("", ListBudgetView.as_view(), name="list-budgets"),
    path("create/", CreateBudgetView.as_view(), name="create-budget"),
    path("update/<int:pk>/", UpdateBudgetView.as_view(), name="update-budget"),
    path("delete/<int:pk>/", DeleteBudgetView.as_view(), name="delete-budget"),
]
