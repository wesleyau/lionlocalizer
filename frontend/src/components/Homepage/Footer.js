import React from 'react';
import { AppBar, Toolbar, Typography, Grid, Tabs, Tab, Button } from "@material-ui/core";
import { createGenerateClassName, makeStyles } from '@material-ui/styles';
import { Route, Switch, Redirect, Link } from "react-router-dom";
import Home from './Home'
import uLogo from '../../../static/images/uLogo.png';
import uLogoOrange from '../../../static/images/uLogoOrange.png';
import USAID from '../../../static/images/Horizontal_RGB_294.png';
import USAIDSEAL from '../../../static/images/Seal_RGB_294.png';

const useStyles = makeStyles({ 
    typography: {
        fontWeight: 'bold',
        marginTop: 10, 
        marginLeft: 5,   
        marginBottom: 10
    },
    image: {
        height: '16%',
        width: '16%'
    },
    sealImage: {
        height: '7%',
        width: '7%',
        marginLeft: 0
    },
})

const Footer = () => {
    
    const classes = useStyles()
    return (
        
        <Grid container>
            <Grid item xs={12}>
                <Typography variant="caption" display="block" className={classes.typography}>
                    The Lion Localizer was made possible by the support of the American people through the United States Agency for International Development (USAID). 
                    The views represented on this website do not necessarily reflect the views of The University of Illinois at Urbana-Champaign, the USAID, or the United States government.
                    
                </Typography>
            </Grid>
            
            <Grid item xs={12}>
                <>
                    <AppBar color="secondary" position="static">
                        <Toolbar>
                            <Tabs>
                                <Tab value='contact' to="/contactus" component={Link} label="Contact Us" />
                                <Tab value='copyright' to="/copy" component={Link} label="copyright" />
                                <Tab value='privacy' to="/priv" component={Link} label="Privacy Policy" />
                                <Tab value='terms' to="/tos" component={Link} label="Terms & Conditions" />
                            </Tabs>
                        </Toolbar>
                    </AppBar>
                </>
            </Grid>    


            <Grid item xs={12}>
                <AppBar position="static">
                    <Toolbar>
                        <img className={classes.image} src={uLogoOrange} />
                        <img className={classes.sealImage} src={USAIDSEAL} />

                    </Toolbar>
                </AppBar>
            </Grid>    
        </Grid>
    );
};

export default Footer;