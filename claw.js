import {
  hDistance,
  vDistance,
  vTopSpace,
  originX,
  originY,
} from "./constants.js";

const vOffsetClaw = -25;
const nofMovers = 20;
const cb0Min = 0.55;
const cb0Max = 0.95;
const cb1Min = 0.1;
const cb1Max = 0.1;
const cb2Min = 0.5;
const cb2Max = 0.6;
const cb3Min = 1.0;
const cb3Max = 1.4;
const clawOpenAngleDegrees = 58;
const clawClosedAngleDegrees = 25;
const ballHolderOffset = 24;

const ipol = (index, min, max, maxIndex) =>
  min + (index * (max - min)) / maxIndex;
const ipolCurried = (min, max, maxIndex) => (index) =>
  ipol(index, min, max, maxIndex);
const ipolCurriedMax = (maxIndex) => (min, max) =>
  ipolCurried(min, max, maxIndex);
const ipolCurriedMaxFun = ipolCurriedMax(nofMovers - 1);
const ipFun0 = ipolCurriedMaxFun(cb0Min, cb0Max);
const ipFun1 = ipolCurriedMaxFun(cb1Min, cb1Max);
const ipFun2 = ipolCurriedMaxFun(cb2Min, cb2Max);
const ipFun3 = ipolCurriedMaxFun(cb3Min, cb3Max);

export const createClaw = () => {
  let claw = {
    clawOpen: false,
    hPosIndex: 0,
    vPosIndex: 0,
    clawLeft: null,
    clawRight: null,
    hMovers: [],
    vMovers: [],
    ballHolderInClawElem: null,
    ballInClaw: null,
  };

  const moversSvg = document.querySelector("#movers-svg");

  const setClawAttributes = (elem) => {
    elem.setAttribute("fill", "none");
    elem.setAttribute("stroke", "black");
    elem.setAttribute("stroke-width", "8");
    elem.setAttribute("transform-origin", `${originX}px ${originY}px`);
    elem.classList.add("claw");
  };

  for (let i = 0; i < nofMovers; i++) {
    const vMover = document.createElementNS("http://www.w3.org/2000/svg", "g");
    vMover.classList.add("v-move");
    claw.vMovers.push(vMover);
    let mover;
    if (i < nofMovers - 1) {
      mover = document.createElementNS("http://www.w3.org/2000/svg", "circle");
      mover.setAttribute("stroke", "none");
      mover.setAttribute("fill", "black");
      mover.setAttribute("cx", `${originX}`);
      mover.setAttribute("cy", `${originY}`);
      mover.setAttribute("r", "11");
      mover.setAttribute("stroke-width", "3");
    } else {
      mover = document.createElementNS("http://www.w3.org/2000/svg", "g");
      const ballHolder = document.createElementNS(
        "http://www.w3.org/2000/svg",
        "g"
      );
      ballHolder.style.transform = `translateY(${ballHolderOffset}px)`;
      mover.appendChild(ballHolder);
      claw.ballHolderInClawElem = ballHolder;
      vMover.classList.add("claw-wrapper");
      claw.clawRight = document.createElementNS(
        "http://www.w3.org/2000/svg",
        "path"
      );
      claw.clawRight.setAttribute("id", "claw-right");
      claw.clawRight.setAttribute(
        "d",
        `M${originX},${originY} a20,20 0 0,1 0,40`
      );
      setClawAttributes(claw.clawRight);
      mover.appendChild(claw.clawRight);

      claw.clawLeft = document.createElementNS(
        "http://www.w3.org/2000/svg",
        "path"
      );
      claw.clawLeft.setAttribute("id", "claw-left");
      claw.clawLeft.setAttribute(
        "d",
        `M${originX},${originY} a20,20 0 0,0 0,40`
      );
      setClawAttributes(claw.clawLeft);
      mover.appendChild(claw.clawLeft);

      const clawHinge = document.createElementNS(
        "http://www.w3.org/2000/svg",
        "circle"
      );
      clawHinge.setAttribute("fill", "black");
      clawHinge.setAttribute("cx", `${originX}`);
      clawHinge.setAttribute("cy", `${originY - 2}`);
      clawHinge.setAttribute("r", "6");
      clawHinge.setAttribute("stroke", "none");
      mover.appendChild(clawHinge);

      const clawBolt = document.createElementNS(
        "http://www.w3.org/2000/svg",
        "circle"
      );
      clawBolt.setAttribute("fill", "white");
      clawBolt.setAttribute("cx", `${originX}`);
      clawBolt.setAttribute("cy", `${originY - 2}`);
      clawBolt.setAttribute("r", "2");
      clawBolt.setAttribute("stroke", "none");
      mover.appendChild(clawBolt);
    }
    const transFun = `cubic-bezier(${ipFun0(i)}, ${ipFun1(i)}, ${ipFun2(
      i
    )}, ${ipFun3(i)}`;
    mover.style["transition-timing-function"] = transFun;
    mover.classList.add("h-move");
    claw.hMovers.push(mover);
    vMover.appendChild(mover);
  }

  claw.vMovers.forEach((vMover) => {
    moversSvg.appendChild(vMover);
  });

  return claw;
};

export const updateClawPosition = (claw) => {
  const hPos = claw.hPosIndex * hDistance;
  console.log(
    `hPosIx: ${claw.hPosIndex} vPosIx: ${claw.vPosIndex} hPos:${hPos}`
  );
  const vPosFun = ipolCurried(
    0,
    vTopSpace + vOffsetClaw + claw.vPosIndex * vDistance,
    claw.vMovers.length - 2
  );
  claw.hMovers.forEach((mover, i) => {
    mover.style.transform = `translateX(${hPos}px)`;
  });
  claw.vMovers.forEach((mover, i) => {
    let index = i;
    let offset = -15;
    if (mover.classList.contains("claw-wrapper")) {
      index = index - 1;
      offset = 1;
    }

    let vPos = vPosFun(index) + offset;
    mover.style.transform = `translateY(${vPos}px)`;
  });
  const clawAngleDegrees = claw.clawOpen
    ? clawOpenAngleDegrees
    : clawClosedAngleDegrees;
  claw.clawRight.style.transform = `rotate(${-clawAngleDegrees}deg)`;
  claw.clawLeft.style.transform = `rotate(${clawAngleDegrees}deg)`;
};
