from rest_framework.generics import (ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView)

from budget.models import Budget
from budget.serializers import BudgetSerializer


class ListBudgetView(ListAPIView):
    """Retrieves all the budgets"""
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer


class CreateBudgetView(CreateAPIView):
    """Create a new budget"""
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer


class UpdateBudgetView(UpdateAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer


class DeleteBudgetView(DestroyAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

