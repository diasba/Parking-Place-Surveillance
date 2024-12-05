import { render, screen, waitFor } from '@testing-library/react';
import '@testing-library/jest-dom'
import App from '../src/App'; // Main app entry point

beforeEach(() => {
  // Mock fetch to avoid external API calls
  global.fetch = jest.fn().mockResolvedValue({
    json: jest.fn().mockResolvedValue([
      { id: 1, occupied: false, prediction: 10 },
      { id: 2, occupied: true, prediction: 5 },
      { id: 3, occupied: false, prediction: 12 },
      { id: 4, occupied: false, prediction: 8 },
      { id: 5, occupied: true, prediction: 3 },
    ]),
  });
});

test('renders all expected components', async () => {
    // Render the application
    render(<App />);

    // Assertions for each component
    expect(screen.getByRole('banner')).toBeInTheDocument(); // check header
    expect(screen.getByText('The App')).toBeInTheDocument(); 

    //Check that the grid is rendered
    await waitFor(() => expect(screen.getByTestId("parking-grid")).toBeInTheDocument());

    //await waitFor(() => expect(screen.getByTestId("parking-spot-card")).toBeInTheDocument());
    
    // Now that we have confirmed the grid is rendered, test for the ParkingSpot cards inside it
    const parkingSpotCards =  await screen.findAllByTestId("parking-spot-card");

    // Check that the correct number of parking spot cards is rendered
    expect(parkingSpotCards.length).toBe(5);

    // Optionally, you can check for specific content inside the ParkingSpot cards
    parkingSpotCards.forEach((card, index) => {
        expect(card).toHaveTextContent(`Parking Spot ${index + 1}`);  // Assumes your ParkingSpot title includes "Parking Spot N"
    })
});
