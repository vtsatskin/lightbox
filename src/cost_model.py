
class SolarPanel(object):
    """Solar Panel type to be used in the model with the following properties:

    Attributes:
        efficency: The manufacturer stated efficiency.
        cost: The cost of a single solar panel_area.
        area: The useful surface area of the panel.
        power: The max power production rating of the panel.
        beta: The temperature coefficient for the solar panel.
        phi: the shading coefficient.
        tau: the degredation coefficient.
    """

    def __init__(self, company, model_number, efficiency, cost, area, power, beta, phi, tau):
        """Define an object with parameters as entered.
        """

        self.company = company
        self.company = company
        self.efficiency = efficiency
        self.cost = cost
        self.area = area
        self.power = power
        self.beta = beta
        self.phi = phi
        self.tau = tau

class SolarArray(object):
    """
        Solar Panel array composed of a given number of specific panels.

        Attributes:
            solar_panel: The specific panel used in the array.
            number_of_panels: The number of panels used in the array.
            total_cost: The cost of all panels in the array (does not include
                associated costs like inverters and wiring).
            array_area: The useful surface area of all the panels.
            production: The max power output of the entire array.

    """
    def __init__(self, solar_panel, number_of_panels):
        """Define an object with parameters as entered and calculate bulk properties."""
        self.solar_panel = solar_panel
        self.number_of_panels = number_of_panels
        self.calculate_array()
    
    def calculate_array():
        """Computes the bulk properties of the array from the current number of panels"""
        self.total_cost = self.solar_panel.cost*self.number_of_panels 
        self.array_area = self.solar_panel.area*self.number_of_panels
        self.production = self.solar_panel.power*self.number_of_panels

    def remove_panels(number):
        """Removes a given number of panels from the array"""
        self.number_of_panels = self.number_of_panels - number
        self.calculate_array()    


class Regulations(object):
    """
        Class containing all relevant regulation and administrative parameters.

        Attributes:
            contract_price: The price at which the home owner sells the energy to the grid.
            power_limit: The maximum production rating of a residential array.
            admin_costs: The administrative costs associated with implementing an array.
    """

    def __init__(self, contract_price, power_limit, admin_costs):
        """Define an object with parameters as entered."""
        self.contract_price = contract_price
        self.power_limit = power_limit
        self.admin_costs = admin_costs

class Installation(object):
    """
        Class containingall relevant Installation information.

        Attributes:
            provider: The Installation provider from which the costs are obtained.
            base_cost: The cost of installing any size array.
            cost_per_panel: The cost of installing an additional panel.
            solar_array: The solar array used for calculations.
            install_cost: The total cost of installing the array.
    """

    def __init__(self, provider, base_cost, cost_per_panel, solar_array):
        """Define an object with parameters as entered."""
        self.provider = provider
        self.base_cost = base_cost
        self.cost_per_panel = cost_per_panel
        self.solar_array = solar_array
        self.total()

    def total():
        """Calculate the total install cost"""
        self.install_cost = self.base_cost + cost_per_panel*solar_array.number_of_panels

class economic_model(object):
    """Class containg all necessary parameters for calculating the economic model.

       Attributes:
            solar_array: The array from which the model is generated.
            installation: Object containing costs and info about installation.
            regulations: Object containing costs and info about regulations.
            production: Object containing cumulative energy production values for all periods.
            years: The number of years the production model was generated for.
            revenue: The total revenue generated over the simulation period.
            costs: The total initial costs assuming no maintenance.
            payback_period: The number of years until the initial costs are paid off.
            return_on_investment: The yearly return on the initial investment as an average.
    """
    def __init__(self, solar_array, installation, regulations, production):
        self.solar_array = solar_array
        self.installation = installation
        self.regulations = regulations
        self.production = production
        self.years = production.years

    def get_revenue():
        """Calculates revenue from contract price and bulk energy produced."""
        self.revenue = regulations.contract_price*production.total_cost
    
    def get_costs():
        """Calculates cost from the totals of each area."""
        self.costs = installation.install_cost + regulations.admin_costs 
        + solar_array.total_cost

    def calculate():
        """Calculates the payback period for the array and the yearly return on investment."""
        ##ToDo: Use actual yearly or monthly values
        yearly_average = self.revenue/self.years
        self.payback_period = self.costs/yearly_average
        self.return_on_investment = yearly_average/self.costs
        
        




