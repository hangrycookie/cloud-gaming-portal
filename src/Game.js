import React, { useState } from 'react';

function Game(props) {
    const { name, image, desc, vmNumber, vmIp, user, password } = props.game;
    const [isVmRunning, setIsVmRunning] = useState(false);
    const [activateLoading, setActivateLoading] = useState(false);

    const startVm = () => {
        setActivateLoading(true);
        fetch(`/api/vm/start/${vmNumber}`).then(res => res.json()).then(data => {
            console.log(data);
            let you = JSON.parse(data.response.toLowerCase());
            setIsVmRunning(you);
            setActivateLoading(false);
        });
    }

    const stopVm = () => {
        setActivateLoading(true);
        fetch(`/api/vm/stop/${vmNumber}`).then(res => res.json()).then(data => {
            console.log(data);
            let you = JSON.parse(data.response.toLowerCase());
            setIsVmRunning(you);
            setActivateLoading(false);
        });
    }

    return (
        <div className="card col-5 m-5">
            {/* <img className="" src="..." alt="Card image cap" /> */}
            <img src={image} className='card-img-top' alt={name} />
            <div className="card-body">
                <h5 className="card-title">{name}</h5>
                <p className="card-text">{desc}</p>
                <button type='button' onClick={startVm} className={`btn btn-success `} disabled={!props.access} hidden={isVmRunning || activateLoading}>Play</button>
                <div className="spinner-border text-dark" hidden={!activateLoading} role="status">
                </div>
                <button type='button' onClick={stopVm} className={`btn btn-danger `} disabled={!props.access} hidden={!isVmRunning || activateLoading}>Stop</button>
                <div className='card m-3 bg-dark text-white border-3' hidden={!isVmRunning}>
                    <span>Connect via RDP</span>
                    <span>{`IP VM : ${vmIp}`}</span>
                    <span>{`USER: ${user}`}</span>
                    <span>{`PASSWORD: ${password}`}</span>
                    <span>Don't forget to add the port 3389 to the IP !</span>
                </div>
            </div>
        </div>
  );
}

export default Game;