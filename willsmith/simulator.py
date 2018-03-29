from agents.human_agent import HumanAgent


class Simulator:
    """
    Manages the game and its state, and prompts agents for actions.
    """

    CLEAR_TERMINAL = chr(27) + "[2J"

    def __init__(self, game, agent_list, time_allowed):
        self.game = game(len(agent_list))
        self.agents = [agent(i) for i, agent in enumerate(agent_list)]
        self.time_allowed = time_allowed

    def advance_by_action(self, action):
        """
        After checking that the action is valid, apply the action to the 
        game state and the agents.
        """
        if self.game.is_legal_action(action):
            self.game.take_action(action)
            for agent in self.agents:
                agent.take_action(action)
    
    def run_game(self):
        """
        Run a console version of the game.
        """
        while not self.game.is_terminal():
            current_agent = self.agents[self.game.current_agent_id]
            action = current_agent.search(self.game.copy(), self.time_allowed)
            self.advance_by_action(action)
            self.display_game()
    
    def display_game(self):
        print(self.CLEAR_TERMINAL)
        print(self.game)

    def add_action_prompt_to_human_agent(self, action_prompt):
        """
        Used to add correct game prompt for HumanAgent to input actions.
        """
        for agent in self.agents:
            if isinstance(agent, HumanAgent):
                agent.action_prompt = action_prompt
