import React, { useState, useEffect } from 'react';
import { AppBar, Toolbar, Typography, Grid, Tabs, Tab } from "@material-ui/core";
import { createGenerateClassName, makeStyles, Classes } from '@material-ui/styles';
import Time from './Time';
import { useDispatch, useSelector } from 'react-redux';


const useStyles = makeStyles({ 
    typography: {

        marginLeft: 10,
        
    },
    linedUp: {
        marginLeft: 10,
        fontFamily: 'courier',
    },
    contain: {
        height: '300px',
    },
    typographyMargin: {
        marginLeft: 10,
        marginTop: 5,
        marginBottom: 10,
        
    },
})


const Input = () => {
    const classes = useStyles()
    
    const alignList = useSelector(state => state.align.align.array)
    const queryInfo = useSelector(state => state.align.align.query)

    const [ID, setID] = useState(queryInfo.ID);
    const [Detail, setDetail] = useState(queryInfo.Detail);

    const detailBreakUp = Detail.match(/[\s\S]{1,114}/g) || ['/n']
    console.log(detailBreakUp)

    return (
        <Grid container className={classes.contain}>  
            <Grid item xs={12}>
                <Typography className={classes.typographyMargin}><Time /></Typography>
            </Grid>     
            <Grid item xs={12}>
                <Typography className={classes.typography}>ID and Sequence Provided:
                 </Typography>
            </Grid>    
            <Grid item xs={12}>
                <Typography className={classes.typography}> {ID} 
                 </Typography>
            </Grid>    
            <Grid item xs={12}>
                 <Typography className={classes.linedUp}> {detailBreakUp.map((index) => (
                     <span>{index} {"\n"}</span>
                 ))}</Typography>
                 
            </Grid>   
            
            <Grid item xs={12}>
                <div className={classes.typographyMargin}> Locations may be shown or removed as pins on the map by clicking on the box next to each location name. 
                    However, this is enabled only for the closest-matching haplotype at each geographic location. Location and closest-haplotype information may also be shown by clicking on an icon or pin on the map itself.
                    </div>
            </Grid> 
        </Grid>
    );
};

export default Input;