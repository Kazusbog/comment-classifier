import { Box, Card, CardContent, Typography, TextField, Button, Paper } from '@mui/material';

export default function Classifier() {
  return (
    <Box sx={{ mt: 4 }}>
      <Typography variant="h4" sx={{ fontWeight: "bold" }} gutterBottom>
        Анализ тональности
      </Typography>
      
      <Card sx={{ mb: 4, boxShadow: 2 }}>
        <CardContent sx={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
          <TextField
            label="Текст комментария"
            multiline
            rows={4}
            variant="outlined"
            placeholder="Вставьте отзыв для проверки..."
            fullWidth
          />
          <Button variant="contained" size="large" sx={{ alignSelf: 'flex-start' }}>
            Анализировать
          </Button>
        </CardContent>
      </Card>

      <Typography variant="h5" gutterBottom>
        Результат:
      </Typography>
      {/* Плашка с демонстрационным ответом */}
      <Paper sx={{ p: 2, bgcolor: '#e8f5e9', color: '#2e7d32', borderLeft: '6px solid #4caf50' }}>
        <Typography variant="h6" sx={{ fontWeight: "bold" }}>Положительный (98%)</Typography>
        <Typography variant="body1" sx={{ mt: 1 }}>
          Текст: "Отличный сервис, мне всё очень понравилось!"
        </Typography>
      </Paper>
    </Box>
  );
}