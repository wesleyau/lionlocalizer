import React, { useState } from 'react';
import { AppBar, Toolbar, Typography, Grid, Button, Select, MenuItem, FormControl, InputLabel } from "@material-ui/core";
import { createGenerateClassName, makeStyles, Classes } from '@material-ui/styles';
import { Route, Switch, Redirect } from "react-router-dom";
import TextField from '@material-ui/core/TextField';

const useStyles = makeStyles({ 
    field: {
        marginTop: 5,
        marginBottom: 10,
        display: 'block'
    },
    text: {
        marginTop: 10,
        marginBottom: 5,
        marginLeft: 5,
        marginRight: 5,
        fontWeight: 'bold',
        display: 'block'
    },
    Button: {
        marginLeft: 10,
    },
    formControl: {
        minWidth: 200,
        marginLeft: 10,
        marginBottom: 5,
    },
    formControl1: {
        minWidth: 200,
        marginLeft: 15,
        marginBottom: 10,
    },
    typography: {
        marginRight: 10,
        fontWeight: 'bold',
    }
})

const Content = () => {
    const classes = useStyles()

    //states to see if textboxes are filled or not
    const [id, setId] = useState('')
    const [sequence, setSequence] = useState('')
    const [idError, setIdError] = useState(false)
    const [sequenceError, setSequenceError] = useState(false)

    //For the dropdown selects
    const [select, setSelect] = useState('')
    const [explore, setExplore] = useState('')
    const [selectError, setSelectError] = useState(false)

    const handleSubmit = (e) => {
        e.preventDefault()
        setSequenceError(false)
        setSequenceError(false)

        if (id == '') {
            setIdError(true)
        }
        if (sequence == '') {
            setSequenceError(true)
        }
        if (id && sequence) {
            console.log(id, sequence)
        }
        if (select == '') {
            setSelectError(true)
        }

    }


    return (
        <Grid container>
            <Grid item xs={12} >
                <form noValidate autoComplete="off" onSubmit={handleSubmit}>
                    <Grid item xs={12}>
                        <Typography className={classes.text}>
                            1. Choose input cytB sequence
                        </Typography>
                    </Grid>   
                    <FormControl className={classes.formControl}>
                        <InputLabel>CytB Regions</InputLabel>
                        <Select value={0} onChange={(e) => setSelect(e.target.value)} error={selectError}>
                            <MenuItem value='0'>1 long cytB region</MenuItem>
                            <MenuItem value='1'>3 Short cytB regions</MenuItem>
                        </Select>
                    </FormControl>
                    <Grid item xs={12}>
                        <Typography className={classes.text}>
                            2. Enter Your Lion Sequence
                        </Typography>
                    </Grid>   
                    <TextField 
                        onChange={(e) => setId(e.target.value)}
                        label="Enter Lion Id"
                        variant="outlined"
                        color="secondary"
                        className={classes.field}
                        fullWidth
                        error={idError}
                    />
                    <TextField 
                        onChange={(e) => setSequence(e.target.value)}
                        label="Enter Lion Sequence"
                        variant="outlined"
                        color="secondary"
                        className={classes.field}
                        multiline
                        rows={4}
                        fullWidth
                        error={sequenceError}
                    />
                    <Button
                        onClick={() => console.log('Sequence submit was clicked')}
                        Type="Submit Query"
                        color="primary"
                        variant="contained"
                        >
                        Submit Query
                    </Button>
                    <FormControl className={classes.formControl1}>
                        <Typography className={classes.typography}>Or select an existing sequence for demonstration: </Typography> 
                            <Select onChange={(e) => setSelect(e.target.value)} error={selectError}>
                                <MenuItem value=''>None</MenuItem>
                                <MenuItem value='1'>LL0001</MenuItem>
                                <MenuItem value='2'>LL0002</MenuItem>
                                <MenuItem value='3'>LL0003</MenuItem>
                                <MenuItem value='4'>LL0004</MenuItem>
                                <MenuItem value='5'>LL0005</MenuItem>
                                <MenuItem value='6'>LL0006</MenuItem>
                            </Select>
                    </FormControl>
                </form>
            </Grid>     
            <Grid item xs={12}>
            </Grid>    
        </Grid>
    );
};

export default Content;