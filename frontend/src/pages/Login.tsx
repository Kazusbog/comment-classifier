import { Box, Card, CardContent, Typography, TextField, Button } from '@mui/material';
import { useNavigate } from 'react-router-dom';

export default function Login() {
  const navigate = useNavigate();

  const handleLogin = () => {
    // Имитация успешного входа: просто перенаправляем пользователя на главный экран
    navigate('/');
  };

  return (
    <Box sx={{ display: 'flex', justifyContent: 'center', mt: 8 }}>
      <Card sx={{ maxWidth: 400, width: '100%', boxShadow: 3 }}>
        <CardContent sx={{ display: 'flex', flexDirection: 'column', gap: 2, p: 4 }}>
          <Typography variant="h5" align="center" sx={{ fontWeight: 'bold' }} gutterBottom>
            Вход в систему
          </Typography>
          
          <TextField label="Логин" variant="outlined" fullWidth />
          <TextField label="Пароль" type="password" variant="outlined" fullWidth />
          
          <Button variant="contained" size="large" onClick={handleLogin} fullWidth>
            Войти
          </Button>
          <Button color="primary" fullWidth>
            Нет аккаунта? Зарегистрироваться
          </Button>
        </CardContent>
      </Card>
    </Box>
  );
}