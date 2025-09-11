# Função para verificar se o usuário está logado
def usuario_id(request):
    return {'usuario_id': request.session.get('usuario_id')}
