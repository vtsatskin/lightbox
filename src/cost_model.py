
class SolarPanel(object):
    """Solar Panel type to be used in the model wit the following properties:

    Attributes:
        efficency: The manufacturer stated efficiency.
        cost: The cost of a single solar panel_area.
        panel_area: The useful surface area of the panel.
        beta: The temperature coefficient for the solar panel
        phi: the shading coefficient
        tau: the degredation coefficient
    """

    def __init__(self, name, efficiency, cost, panel_area, beta, phi, tau):
        """Define an object with name "name" and parameters as entered.
        """

        self.name = name
        self.efficiency = efficiency
        self.cost = cost
        self.panel_area = panel_area
        self.beta = beta
        self.phi = phi
        self.tau = tau



class Regulations(object):
    """
    """

    def __init__(self, contract_price, power_limit, admin_costs):
        """
        """
        self.contract_price = contract_price
        self.power_limit = power_limit
        self.admin_costs = admin_costs

class Installation(object):
    """
    """

    def __init__(self, provider, base_cost, cost_per, solar_)



