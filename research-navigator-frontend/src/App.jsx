import Upload from "./components/Upload/Upload";
import Chat from "./components/Chat/Chat";


function App() {
  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <h1 className="text-3xl font-bold text-center mb-6">
        🚀 ResearchNavigator AI
      </h1>

      <div className="grid md:grid-cols-2 gap-6">
        <Upload />
        <Chat />
      </div>
    </div>
  );
}

export default App;