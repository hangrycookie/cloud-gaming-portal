import React, { useState, useEffect, useRef } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import logo from './logo.svg';
import './App.css';
import Header from './Header';
import Home from './Home';

function App() {
  const [currentTime, setCurrentTime] = useState(0);
  const user = useRef();
  const password = useRef();
  const [currentUser, setCurrentUser] = useState('');
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [tryCount, setTryCount] = useState(0);
  const [userAccess, setUserAccess] = useState(false);

  useEffect(() => {
    fetch('/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
  }, []);

  const addUser = () => {
    fetch('/api/users', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({'username': user.current.value, 'password': password.current.value, 'access': true})
    }).then(res => res.json()).then(data => {
      console.log(data)
    });
  }

  const checkUser = () => {
    fetch('/api/resource', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({'username': user.current.value, 'password': password.current.value})
    }).then(res => res.json()).then(data => {
      console.log(data);
      setTryCount(tryCount + 1);
      setIsLoggedIn(data.response === 'true');
      setUserAccess(data.access);
      setCurrentUser(data.username);
    });
  }

  return (
    <div className="App">
      <Header />
      {
        isLoggedIn && tryCount > 0 ?
        <Home user={currentUser} access={userAccess} />
        :
        <header className="App-header">
        Login
        {/* <p>The current time is {currentTime}.</p> */} 
        <div className='flex justify-content-left col-3 card m-5 border-0'>
          <label className=' text-dark' for='user'>User</label>
          <input id='user' ref={user} className='form-control' type='text' />
          <label className=' text-dark' for='user'>Password</label>
          <input ref={password} className='form-control' type='password' />
          <button type='button' className='btn btn-primary' onClick={addUser}>Add User</button>
          <button type='button' className='btn btn-danger' onClick={checkUser}>Verify User</button>
        </div>
        {
          !isLoggedIn && tryCount > 0 ?
          <div>
            Erreur d'authentification : Utilisateur ou mot de passe erroné
          </div> : null 
        }
        </header>
      }
    </div>
  );
}

export default App;