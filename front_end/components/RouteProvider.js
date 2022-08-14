import React, { useContext, useState } from 'react';

const RouteContext = React.createContext()
const RouteUpdateContext = React.createContext()

export const useRoute = () => {
    return useContext(RouteContext)
}

export const useRouteUpdate = () => {
    return useContext(RouteUpdateContext)
}


export const RouteProvider = ({children}) => {
    const [ route, setRoute ] = useState({})

    const updateRoute = (currentRoute) => {
        setRoute(currentRoute)
    }

    return (
        <RouteContext.Provider value={route}>
            <RouteUpdateContext.Provider value={updateRoute}>
                {children}
            </RouteUpdateContext.Provider>
        </RouteContext.Provider>
    )
}