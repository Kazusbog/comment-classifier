import { Box, Typography, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, Chip } from '@mui/material';

// Демонстрационные данные
const demoHistory = [
  { id: 1, text: 'Отличный сервис, мне всё очень понравилось!', result: 'Позитивный', color: 'success' as const },
  { id: 2, text: 'Приложение постоянно вылетает, ужасно.', result: 'Негативный', color: 'error' as const },
  { id: 3, text: 'Нормально, но дизайн мог бы быть и лучше.', result: 'Позитивный', color: 'success' as const },
];

export default function History() {
  return (
    <Box sx={{ mt: 4 }}>
      <Typography variant="h4" sx={{ fontWeight: "bold" }} gutterBottom>
        История проверок
      </Typography>
      
      <TableContainer component={Paper} sx={{ boxShadow: 2, mt: 3 }}>
        <Table>
          <TableHead sx={{ bgcolor: '#f5f5f5' }}>
            <TableRow>
              <TableCell sx={{ fontWeight: 'bold' }}>ID</TableCell>
              <TableCell sx={{ fontWeight: 'bold' }}>Текст комментария</TableCell>
              <TableCell sx={{ fontWeight: 'bold' }}>Результат</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {demoHistory.map((row) => (
              <TableRow key={row.id} hover>
                <TableCell>{row.id}</TableCell>
                <TableCell>{row.text}</TableCell>
                <TableCell>
                  <Chip label={row.result} color={row.color} size="small" sx={{ fontWeight: 'bold' }} />
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Box>
  );
}