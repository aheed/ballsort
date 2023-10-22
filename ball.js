import { originX, originY } from "./constants.js";

const _createBallCircle = (color) => {
  const ret = document.createElementNS("http://www.w3.org/2000/svg", "circle");
  ret.setAttribute("stroke", "black");
  ret.setAttribute("fill", color);
  ret.setAttribute("cx", `${originX}`);
  ret.setAttribute("cy", `${originY}`);
  ret.setAttribute("r", "18");
  ret.setAttribute("stroke-width", "2");
  ret.classList.add("ball");
  return ret;
};

const _createBallLabel = (text) => {
  const ret = document.createElementNS("http://www.w3.org/2000/svg", "text");
  ret.setAttribute("x", `${originX - 6}`);
  ret.setAttribute("y", `${originY + 6}`);
  ret.setAttribute("font-size", "20");
  ret.setAttribute("font-weight", "bold");
  ret.setAttribute("font-family", "arial");

  const tspan = document.createElementNS("http://www.w3.org/2000/svg", "tspan");
  tspan.setAttribute("dx", "6");
  tspan.textContent = text;
  tspan.style["text-align"] = "center";
  tspan.style["text-anchor"] = "middle";

  ret.appendChild(tspan);
  return ret;
};

export const createBallWrapper = (color, text) => {
  const coloredBall = _createBallCircle(color);
  const label = _createBallLabel(text);
  const wrapper = document.createElementNS("http://www.w3.org/2000/svg", "g");
  wrapper.classList.add("ball-wrapper");
  wrapper.appendChild(coloredBall);
  wrapper.appendChild(label);
  return wrapper;
};

export const createBall = (hIndex, vIndex, color, text, id) => {
  const moversSvg = document.querySelector("#movers-svg");
  const wrapper = createBallWrapper(color, text);
  moversSvg.appendChild(wrapper);
  return {
    hIndex: hIndex,
    vIndex: vIndex,
    wrapper: wrapper,
    color: color,
    text: text,
    id: id
  };
};

export const updateBall = ({wrapper, color, text}) => {
  const circle = wrapper.querySelector("circle");
  circle.setAttribute("fill", color);
  const tspan = wrapper.querySelector("tspan");
  tspan.textContent = text;
}