def cancerRisk(history, european, cn, haplo):
    if not history:
        return False
    elif european=="Yes":
        if haplo=='AA':
            return 'Low Risk'
        else:
            return 'High Risk'
    elif european=="Mixed":
        if halpo!='AA':
            return 'High Risk'
        elif cn<16:
            return 'Medium Risk'
        else:
            return 'Low Risk'
    else:
        if cn<16:
            if haplo == 'AA':
                return 'Medium Risk'
            else:
                return 'High Risk'

    