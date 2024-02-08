import React from 'react';
import { useIntl } from 'react-intl';
import { Box, Typography } from '@mui/material';
import { COLORS } from '../styles/colors';
import '../styles/Footer.css';

const Footer = () => {
  //const footerText = intl.formatMessage({ id: 'footerText' });
  return (        <Box
    component="footer"
    className='footer'
>
    <Typography variant="body2" gutterBottom sx={{
        color: "white",
    }}>
        {"Manage your tasks effortlessly with TaskManager. Organize, prioritize, and stay productive."}
    </Typography>
</Box>
  );
}
const boxStyle = {
  backgroundColor: COLORS.dark,

  position: 'fixed',
  bottom: 0,

  width: '100%',
  zIndex: 1,
  right: '0px',
  left: '0px',
  height: '30px',

  display: 'flex',
  alignItems: 'center',
  justifyContent: 'center',
};
export default Footer;