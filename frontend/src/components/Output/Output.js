import React, { useState, useEffect, } from 'react';
import { Route, Redirect } from 'react-router'
import { AppBar, Toolbar, Typography, Grid, Tabs, Tab, ThemeProvider } from "@material-ui/core";
import { makeStyles } from '@material-ui/styles';
import Map from './Map1';
import Table2 from './Table2';
import Input from './Input';
import { useDispatch, useSelector } from 'react-redux';
import { getSequences } from '../../Sequences/Sequences.actions';



const useStyles = makeStyles({ 
    print: {
        display: 'inline',
        overflowY: 'scroll',
        
    },
    disclaimer: {
        marginTop: 5, 
        marginLeft: 5,   
    },
    abbreviation: {
        marginTop:5, 
        marginLeft: 5,
        
    }
    
})


const Output = () => {
    const classes = useStyles()
    const dispatch = useDispatch();

    const test = useSelector(state => state)
    const seqList = useSelector(state => state.sequences.sequences)
    const alignList = useSelector(state => state.align.align.array)
    const queryInfo = useSelector(state => state.align)
    

    //state for the checkmarks to what is displayed on the map
    const [check, setCheck] = useState()
    const [loading, setLoading] = useState(false)

    //if(!queryInfo) {
    //return <Redirect to="/"/>
   //}


    return (
        <Grid container>
            <Grid item container >
                <Grid xs = {6}>
                    {queryInfo.isLoading == true && (
                        <div>Loading...</div>
                    )}
                    {queryInfo.isLoading == false && (
                        <Map check={check}/>
                    )}
                </Grid>
                <Grid item container xs={6}>
                    <Grid item container  xs={12}>
                        <Grid className={classes.print} xs = {12}>
                            {queryInfo.isLoading == true && (

                                <div>Loading...</div>
                            )}
                            {queryInfo.isLoading == false && (

                                <Input />
                            )}
                         </Grid>
                        <Grid className={classes.print} xs = {12}>
                            {queryInfo.isLoading == true && (
                                <div>Loading...</div>
                            )}
                            {queryInfo.isLoading == false && (
                                <Table2 setCheck={setCheck} />
                            )}
                        </Grid>
                    </Grid>
                </Grid>
            </Grid> 
            <Grid item xs={12}>
                <Typography variant="caption" display="block" className={classes.abbreviation}>Abbreviations: FR: Forest Reserve GR: Game Reserve, NP: National Park, WS: Wildlife Sanctuary</Typography>
            </Grid>  
            <Grid item xs={12} direction="row">
                    <Typography variant="caption" display="block" className={classes.disclaimer}> For printing purposes, the Chrome or Safari browsers are recommended, the printout may not be formatted as well by Firefox </Typography>
            </Grid> 
        </Grid>
    );
};


export default Output;