import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { Container, CssBaseline } from "@mui/material";
import Navbar from "./components/Navbar";
import Login from './pages/Login';
import Classifier from "./pages/Classifier";
import History from "./pages/History";

export default function App() {
  return (
    <BrowserRouter>
    {/* CssBaseLine сбросит дефолтные настройки браузера и поставит шрифт MUI */}
    <CssBaseline />

    {/* навигационная панель будет отображаться на всех экранах */}
    <Navbar />
    {/* container ограничит ширину контента, а mt: 4 сделает отступ сверху */}
    <Container maxWidth="md" sx={{ mt: 4}}>
      <Routes>
      {/* Путь к странице входа */}
      <Route path="/login" element={<Login />} />

      {/* Путь к странице с классификатором (главной) */}
      <Route path="/" element={<Classifier />} />

      {/* Страница истории */}
      <Route path="/history" element={<History />} />

      {/* Incorrect адрес */}
      <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </Container>
      
    </BrowserRouter>
  )
}