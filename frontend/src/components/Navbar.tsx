import {AppBar, Toolbar, Typography, Button, Box } from '@mui/material';
import {Link } from 'react-router-dom';

export default function Navbar() {
    return (
        <AppBar position='static'>
            <Toolbar>
                {/* название прилы */}
                <Typography variant='h6' sx={{ flexGrow: 1}}>
                    Классификатор 
                </Typography>

                {/* кнопки навигации */}
                <Box>
                    <Button color='inherit' component={Link} to="/">Анализ</Button>
                    <Button color='inherit' component={Link} to="/history">История</Button>
                    <Button color='inherit' component={Link} to="/login">Выход</Button>
                </Box>
            </Toolbar>
        </AppBar>
    );
}