import "./App.css";
import { Grid } from "@mui/material";
import WebpageCard from "./LandingPage/LandingPage";

function App() {
  return (
    <div
      className="App"
      style={{ backgroundColor: "blue", paddingInline: "25px" }}
    >
      <Grid container spacing={12} border={12}>
        <Grid item xs={3}>
          <WebpageCard title={"TSLA"} imgsrc={"./TSLA.png"} />
        </Grid>
        <Grid item xs={3}>
          <WebpageCard title={"AAPL"} imgsrc={"./AAPL.png"} />
        </Grid>
        <Grid item xs={3}>
          <WebpageCard title={"AMZN"} imgsrc={"./AMZN.png"} />
        </Grid>
        <Grid item xs={3}>
          <WebpageCard title={"FB"} imgsrc={"./FB.png"} />
        </Grid>
        <Grid item xs={3}>
          <WebpageCard title={"GOOG"} imgsrc={"./GOOG.png"} />
        </Grid>
        <Grid item xs={3}>
          <WebpageCard title={"COF"} imgsrc={"./COF.png"} />
        </Grid>
        <Grid item xs={3}>
          <WebpageCard title={"GM"} imgsrc={"./GM.png"} />
        </Grid>
        <Grid item xs={3}>
          <WebpageCard title={"F"} imgsrc={"./F.png"} />
        </Grid>
        <Grid item xs={3}>
          <WebpageCard title={"NVDA"} imgsrc={"./NVDA.png"} />
        </Grid>
      </Grid>
    </div>
  );
}

export default App;
