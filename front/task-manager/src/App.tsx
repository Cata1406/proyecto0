import "./styles/App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Header from "./components/Header";
import Footer from "./components/Footer";
import TasksPage from "./pages/TasksPage";
import LoginPage from "./pages/LoginPage";
import RegisterPage from "./pages/RegisterPage";
import { Login } from "@mui/icons-material";

function App() {
    return (
        <div className="App">
            <Header />
            <BrowserRouter>
                <Routes>
                    <Route path="/" element={<TasksPage />} />
                    <Route path="/login" element={<LoginPage />} />
                    <Route path="/register" element={<RegisterPage />} />
                </Routes>
            </BrowserRouter>

            <Footer />
        </div>
    );
}

export default App;
