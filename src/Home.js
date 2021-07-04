import React, { useState, useEffect, useRef } from 'react';
import { games } from './data';
import Game from './Game';

function Home(props) {
    const user = props.user;
    const access = props.access;
    return (
    <div className='row'>
        <div className='col-4 game-on bg-danger'>
            <span className='game-on-text'>{access ? 'Game on, ': 'Enjoy the visit,'} {user}</span>
        </div>
        <div className='col-8'>
            <div className='row'>
                {games.map((game) => (
                    <Game game={game} access={access} />
                ))}
            </div>
        </div>
    </div>
  );
}

export default Home;