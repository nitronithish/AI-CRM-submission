import InteractionForm from "../components/InteractionForm";
import ChatInterface from "../components/ChatInterface";

function LogInteraction() {
  return (
    <div className="container">
      <h1>AI-First CRM</h1>
      <h2>Log Interaction</h2>

      <hr />

      <InteractionForm />

      <hr />

      <ChatInterface />
    </div>
  );
}

export default LogInteraction;