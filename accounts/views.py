from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from accounts.managers import AccountManager
from accounts.models import Account, TradeLog


class AccountViewSet(viewsets.GenericViewSet):
    queryset = Account.objects.all()
    # serializer_class =
    # todo: User 구현 되고 IsAuthenticated 로 변경
    permission_classes = [AllowAny]


    def create(self, request):
        """
        계좌생성
        POST /accounts/
        """
        pass

    def retrieve(self, request, pk):
        """
        계좌 단건 조회
        GET /accounts/{account_id}/
        """
        manager = AccountManager()
        account = manager.get_account(request.user, pk)
        pass

    def list(self, request):
        """
        todo: 필요 없으면 삭제, 유저 정보 조회에서 처리할 수도?
        계좌 리스트 조회
        GET /accounts/
        """
        pass

    @action(methods=['POST'], detail=True)
    def deposit(self, request, pk):
        """
        입금
        POST /accounts/{account_id}/deposit/
        """
        manager = AccountManager()
        account = manager.get_account(request.user, pk)
        account, trade_log = manager.deposit(account, request.data)
        # todo: 성공 리스폰스 처리
        return Response(status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=True)
    def withdrawal(self, request, pk):
        """
        출금
        POST /accounts/{account_id}/withdrawal/
        """
        manager = AccountManager()
        account = manager.get_account(request.user, pk)
        account, trade_log = manager.withdrawal(account, request.data)
        # todo: 성공 리스폰스 처리
        return Response(status=status.HTTP_200_OK)
