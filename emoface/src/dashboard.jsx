import React from 'react'
import Search from './search.jsx';
import Selfie from './Selfie';

export default function Dashboard() {
    return (
        <div clasName="dashboard">
            <Search className="search" />
            <Selfie className="selfie" />           
        </div>
    )
}
