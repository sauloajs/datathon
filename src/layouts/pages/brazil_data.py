from src.graphs.line_graphs import plot_poverty_rate_graph, plot_life_expectation_graph, plot_murder_rate_graph

def getHeader():
    return """
        <div class="d-flex w-100 pt-5 ps-5 pe-5" style="flex-direction: column;">
            <div class="d-flex flex-column">
                <h2 class="color--title">
                    <hr class="line--light w-25">
                    A qualidade de vida tem melhorado no Brasil
                    <hr class="line--light w-100">
                </h2>
                <div class="d-flex w-100 justify-content-between">
                    <div class="w-50">
                        <h5 class="color--subtitle">
                            Redução da pobreza no Brasil
                            <hr class="line--orange w-100">
                        </h5>
                    </div>
                    <div class="w-50">
                        <h5 class="color--subtitle">
                            A expectativa de vida aumentou nos últimos 10 anos
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
                    <div class="w-50">
                        <h5 class="color--subtitle">
                            População vivendo em favelas reduziu 20% em 16 anos
                            <hr class="line--orange w-100">
                        </h5>
                    </div>
                    <div class="w-50">
                        <h5 class="color--subtitle">
                            Criminalidade persiste como risco a população
                            <hr class="line--orange w-100">
                        </h5>
                    </div>
                </div>
            </div>
        </div>
    """
    
def getFirstRowGraphs():
    return f"""
        <div class="d-flex w-100 pt-1" style="flex-direction: column;">
            <div class="d-flex container flex-column">
                <div class="d-flex w-100 justify-content-between">
                    <div class="w-50">
                        {plot_poverty_rate_graph()}
                    </div>
                    <div class="w-50">
                        {plot_life_expectation_graph()}
                    </div>
                </div>
            </div>
        </div>
    """