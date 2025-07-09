//import { useState } from 'react'
//import {link} from 'react-router-dom'
//import { useNavigate } from 'react-router-dom'


function HomePage() {
    function Hero() {
        return (
          <section className="hero">
            <h1 className="heroText"> Nutrition Recommender using TinyLlama</h1>
          </section>
        );
      }
      
      return(
        <>
        <Hero />
        </>
      );

}



export default HomePage;