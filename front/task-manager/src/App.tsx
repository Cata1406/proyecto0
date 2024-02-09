import "./styles/App.css";
import { Routes, Route } from "react-router-dom";
import Header from "./components/Header";
import Footer from "./components/Footer";
import TasksPage from "./pages/TasksPage";

function App() {
    return (
        <div className="App">
            <Header />
            <TasksPage />
            <Footer />
        </div>
    );
}

export default App;
