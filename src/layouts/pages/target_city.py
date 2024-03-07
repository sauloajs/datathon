def getHeader():
    return """
        <div class="d-flex w-100 pt-5 ps-5 pe-5" style="flex-direction: column;">
            <div class="d-flex flex-column">
                <h2 class="color--title">
                    <hr class="line--light w-25">
                    A jornada da educação: Embu-Guaçu x Brasil
                    <hr class="line--light w-100">
                </h2>
                <div class="d-flex w-100 justify-content-between">
                    <div class="w-50">
                        <h5 class="color--subtitle">
                            Matrículas concentradas no Ensino Fundamental
                            <hr class="line--orange w-100">
                        </h5>
                    </div>
                    <div class="w-50">
                        <h5 class="color--subtitle">
                            Salários menos atrativos para reter professores
                            <hr class="line--orange w-100">
                        </h5>
                    </div>
                </div>
            </div>
        </div>
    """
    
def getSubHeader():
    return """
        <div class="d-flex w-100 pt-5 ps-5 pe-5" style="flex-direction: column;">
            <div class="d-flex flex-column">
                <div class="d-flex w-100 justify-content-between">
                    <hr class="line--light w-50"/>
                    <hr class="line--light w-50"/>
                </div>
                <div class="d-flex w-100 justify-content-between">
                    <div class="w-50">
                        <h5 class="color--subtitle">
                            Maior parte das escolas é dependente da administração pública
                            <hr class="line--orange w-100">
                        </h5>
                    </div>
                    <div class="w-50">
                        <h5 class="color--subtitle">
                            Abaixo da média nacional e estadual de distorção idade-série
                            <hr class="line--orange w-100">
                        </h5>
                    </div>
                </div>
            </div>
        </div>
    """
    
def getSubHeader2():
    return """
    <div class="d-flex w-100 pt-5 ps-5 pe-5" style="flex-direction: column;">
        <div class="d-flex flex-column">
            <div class="d-flex w-100 justify-content-between">
                <div class="w-100 text-center">
                    <hr class="line--light w-100"/>
                    <h5 class="color--subtitle">
                        Maior parte das escolas é dependente da administração pública
                        <hr class="line--orange w-100">
                    </h5>
                </div>
            </div>
        </div>
    </div>
    """
    
def subtitle(text, hr = False):
    return f"""
    <div class="d-flex w-100 ps-5 pe-5" style="flex-direction: column;">
        <div class="d-flex flex-column">
            <div class="d-flex w-100 justify-content-between">
                <div class="w-100 text-center">
                    <hr class="line--light w-100" />
                    <h5 class="color--subtitle">
                        {text}
                        <hr class="line--orange w-25">
                    </h5>
                </div>
            </div>
        </div>
    </div>
    """ if hr else f"""
    <div class="d-flex w-100 ps-5 pe-5" style="flex-direction: column;">
        <div class="d-flex flex-column">
            <div class="d-flex w-100 justify-content-between">
                <div class="w-100 text-center">
                    <h5 class="color--subtitle">
                        {text}
                        <hr class="line--orange w-25">
                    </h5>
                </div>
            </div>
        </div>
    </div>
    """