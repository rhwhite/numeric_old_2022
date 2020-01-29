"""
    This module contains four finite differencing functions

    return (theTime, theTemp)


def leapfrog(npts, tend, To, Ta, theLambda):
    dt = tend / npts
    theTemp = np.empty([npts,], np.float64)
    theTemp[0] = To
    theTime = np.empty_like(theTemp)
    # estimate first step by forward euler as need two steps to do leapfrog
    theTemp[1] = To + heat(To, Ta, theLambda) * dt
    theTime[1] = dt
    # correct first step by estimating the temperature at a half-step
    Th = To + 0.5 * (theTemp[1] - To)
    theTemp[1] = To + heat(Th, Ta, theLambda) * dt
    for timeStep in np.arange(2, npts):
        theTime[timeStep] = theTime[timeStep - 1] + dt
        theTemp[timeStep] = (
            theTemp[timeStep - 2]
            + heat(theTemp[timeStep - 1], Ta, theLambda) * 2.0 * dt
        )
    return (theTime, theTemp)


def midpoint(npts, tend, To, Ta, theLambda):
    dt = tend / npts
    theTemp = np.empty([npts,], np.float64)
    theTemp[0] = To
    theTime = np.empty_like(theTemp)
    # estimate first step by forward euler as need two steps to do leapfrog
    theTemp[1] = To + heat(To, Ta, theLambda) * dt
    theTime[1] = dt
    # correct first step by estimating the temperature at a half-step
    Th = To + 0.5 * (theTemp[1] - To)
    theTemp[1] = To + heat(Th, Ta, theLambda) * dt
    for timeStep in np.arange(2, npts):
        theTime[timeStep] = theTime[timeStep - 1] + dt
        theTemp[timeStep] = (
            theTemp[timeStep - 2]
            + heat(theTemp[timeStep - 1], Ta, theLambda) * 2.0 * dt
        )
    return (theTime, theTemp)


def runge(npts, tend, To, Ta, theLambda):
    dt = tend / npts
    theTemp = np.empty([npts,], np.float64)
    theTemp[0] = To
    theTime = np.empty_like(theTemp)
    theTime[0] = 0
    for i in np.arange(1, npts):
        k1 = dt * heat(theTemp[i - 1], Ta, theLambda)
        k2 = dt * heat(theTemp[i - 1] + (0.5 * k1), Ta, theLambda)
        k3 = dt * heat(theTemp[i - 1] + (0.5 * k2), Ta, theLambda)
        k4 = dt * heat(theTemp[i - 1] + k3, Ta, theLambda)
        theTemp[i] = theTemp[i - 1] + (1.0 / 6.0) * (k1 + (2.0 * k2) + (2.0 * k3) + k4)
        theTime[i] = theTime[i - 1] + dt
    return (theTime, theTemp)
