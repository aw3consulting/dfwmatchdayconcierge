# DFW AI Intake Question Bank v1.0.0

## 1. Purpose

This file defines the governed AI-assisted intake question bank for DFW Matchday Concierge. It provides the structured question sequence required to generate a Personal Matchday Command Hub Preview, support operator review, and prepare a client-specific concierge plan.

This question bank must be used by the AI-assisted intake layer, intake forms, future command hub logic, and operator-review workflows.

## 2. Governing Principle

The intake sequence must be inquiry-first, not ride-first.

The AI must first understand who the client is, how long they are in Dallas / Fort Worth, what obligations they have, what privacy level applies, what services they may need, and what budget range they are considering.

Transportation is one service category inside the full concierge plan.

## 3. Intake Structure

The question bank is divided into phases:

1. Access and verification readiness
2. Lane selection
3. VIP / sensitive-status handling
4. Trip dates
5. Airport arrival and departure
6. Hotel / housing locations
7. Matchday attendance
8. Obligations and required locations
9. Transportation needs
10. Food, snacks, beverages, and cooler needs
11. Luggage coordination
12. Sightseeing and DFW experience interests
13. Private security interest
14. Guests and party structure
15. Budget and payment readiness
16. Privacy and communication preferences
17. Final review and missing details

## 4. Phase 1: Access and Verification Readiness

Purpose:
Determine whether the visitor is ready to continue into secure intake.

Questions:

1. What email address should we use to send your secure access code or continuation link?
2. What mobile number should we use for urgent matchday coordination or verification if needed?
3. What is your preferred contact method?
   - Email
   - SMS
   - WhatsApp
   - Phone call
4. Are you completing this intake for yourself or on behalf of someone else?
   - Myself
   - Family member
   - VIP guest
   - Executive / client
   - Media / corporate group
   - Team or federation guest
   - Other

Governance:
Do not collect sensitive itinerary, hotel, guest, budget, or payment details before secure access is established.

## 5. Phase 2: Lane Selection

Purpose:
Classify the inquiry lane.

Primary question:

`Which matchday lane best fits your trip?`

Options:

- VIP Guest Concierge
- Team Family Support
- Media / Corporate
- Team Fan Hub
- Not sure / Ask Concierge

Follow-up:

1. Are you seeking full concierge planning or a specific service?
   - Full stay / full concierge
   - Matchday plan
   - Transportation only
   - Food / beverage / cooler support
   - Luggage support
   - Security coordination
   - Not sure yet

## 6. Phase 3: VIP / Sensitive-Status Handling

Purpose:
Allow status disclosure without forcing sensitive disclosure.

Primary question:

`Would you like to disclose VIP, credential, team-family, sponsor, or media context now?`

Options:

- Yes, I can disclose now
- I prefer to disclose after verification
- I prefer not to disclose unless contacted directly
- A representative or assistant will provide details
- This does not apply

Conditional questions if yes:

1. Which context applies?
   - VIP guest
   - Team family member
   - Federation guest
   - Team staff family
   - Sponsor / hospitality guest
   - Media / credentialed guest
   - Guest of credential holder
   - Executive / corporate guest
   - Other
2. Is privacy-sensitive handling requested?
   - Yes
   - No
   - Not sure

Governance:
Do not request credential uploads, relationship proof, celebrity status, or official access proof in the initial AI intake.

## 7. Phase 4: Trip Dates

Purpose:
Establish service window.

Questions:

1. What date do you arrive in Dallas / Fort Worth?
2. What date do you depart Dallas / Fort Worth?
3. Is your stay:
   - Full stay support
   - Weekly support
   - Multi-day support
   - Matchday only
   - Single route only
   - Not sure
4. Are there any dates where concierge support is most important?

## 8. Phase 5: Airport Arrival and Departure

Purpose:
Capture airport and aviation logistics.

Arrival questions:

1. Which airport are you arriving at?
   - DFW International Airport
   - Dallas Love Field
   - Private airport / FBO
   - Other
   - Not sure yet
2. What is your arrival date and estimated arrival time?
3. Is flight tracking or arrival monitoring needed?
4. Will you need airport pickup, luggage help, or hotel transfer?

Departure questions:

1. Which airport are you departing from?
   - DFW International Airport
   - Dallas Love Field
   - Private airport / FBO
   - Other
   - Not sure yet
2. What is your departure date and estimated departure time?
3. Will you need return-to-airport movement?
4. Will you need luggage coordination before departure?

Private airport/FBO follow-up:

1. Do you know the FBO name or private arrival location?
2. Are arrival instructions, handler contact, or security notes available?

## 9. Phase 6: Hotel / Housing Locations

Purpose:
Map stay locations and stay periods.

Questions:

1. Where will you stay during your visit?
   - Hotel
   - Private residence
   - Rental home
   - Team/federation lodging
   - Not confirmed yet
2. What is the hotel or housing location?
3. What dates will you stay at this location?
4. Will your stay location change during the trip?
5. If yes, what are the additional locations and dates?

Privacy rule:
Exact address may be deferred until verified or activated hub state.

## 10. Phase 7: Matchday Attendance

Purpose:
Determine matchday planning needs.

Questions:

1. Which matchday or matchdays will you attend?
2. Which team or country are you supporting or connected to?
3. How many guests will attend the match?
4. Do you need stadium arrival planning?
5. Do you need post-match pickup or return movement?
6. Do you need food, drinks, cooler, or comfort items before matchday?
7. Do you need support for multiple matchdays?

Governance:
Do not claim official ticketing, ticket validation, or official tournament affiliation.

## 11. Phase 8: Obligations and Required Locations

Purpose:
Capture non-match obligations.

Questions:

1. Do you have any required locations during your stay?
   - Stadium
   - Practice facility
   - Media center
   - Sponsor event
   - Corporate event
   - Restaurant reservation
   - Shopping / errands
   - Private outing
   - Other
2. Please list each location, date, and time window if known.
3. Are any obligations privacy-sensitive?
4. Are any locations credential-controlled or access-controlled?
5. Do you need movement between obligations?

Governance:
Credential-controlled locations must be described as client-provided access details, not as access guaranteed by DFW Matchday Concierge.

## 12. Phase 9: Transportation Needs

Purpose:
Identify movement requirements.

Questions:

1. What transportation support do you need?
   - VIP Tahoe / private concierge review
   - Private transportation
   - Airport transfer
   - Hotel to stadium
   - Stadium return
   - Hotel-stadium-airport route
   - Shared ride request
   - Group movement
   - Driver block
   - Not sure
2. How many passengers will ride?
3. How much luggage or equipment will travel?
4. Do you need multiple vehicles?
5. Is privacy-sensitive transportation required?

VIP rule:
Tahoe eligibility must be reviewed by operator and is not guaranteed during intake.

## 13. Phase 10: Food, Snacks, Beverages, and Cooler Needs

Purpose:
Identify concierge add-ons and monetization opportunities.

Questions:

1. Are you interested in food support?
   - Restaurant pickup
   - Local recommendations
   - Team/country-inspired recommendations
   - Catering
   - Grocery stop
   - Not needed
2. Are you interested in snacks or drinks?
3. Are you interested in cooler setup?
4. Do you need coffee, water, ice, cups, or comfort items?
5. Are there dietary preferences or restrictions?

Governance:
Alcohol handling must remain lawful and controlled. Do not promise alcohol delivery unless legality and process are confirmed.

## 14. Phase 11: Luggage Coordination

Purpose:
Capture baggage and storage needs.

Questions:

1. Do you need luggage coordination?
2. How many bags are expected?
3. Are there oversized bags, equipment, media gear, or team/family items?
4. Do you need luggage moved between airport, hotel, stadium, or another location?
5. Do you need temporary luggage storage?

Governance:
Luggage capacity depends on passenger count, bag count, vehicle assignment, and comfort review.

## 15. Phase 12: Sightseeing and DFW Experience Interests

Purpose:
Identify trip-value opportunities beyond matchday.

Questions:

1. Are you interested in sightseeing during your stay?
2. Which areas interest you?
   - Dallas
   - Arlington
   - Fort Worth Stockyards
   - Sundance Square
   - Grapevine
   - FIFA Fan Experience
   - Food districts
   - Shopping
   - Nightlife
   - Not sure
3. Do you want recommendations near where you are staying?
4. Do you want a Dallas/Fort Worth day plan built into your itinerary?

## 16. Phase 13: Private Security Interest

Purpose:
Identify security coordination interest while controlling claim risk.

Questions:

1. Are you interested in private security coordination?
   - Yes
   - No
   - Maybe / discuss privately
2. Is security related to public profile, family privacy, media attention, or general comfort?
3. Should this be discussed only after verified contact?

Governance:
Security must be described as coordination by request until provider model is verified.

## 17. Phase 14: Guests and Party Structure

Purpose:
Prepare activated hub guest fields.

Questions:

1. How many total guests are included in your party?
2. Are there adults, children, elderly guests, or guests needing comfort considerations?
3. Will all guests travel together or split into groups?
4. Will a representative, assistant, or coordinator manage the trip?

Detailed guest names may be deferred until activated hub state.

## 18. Phase 15: Budget and Payment Readiness

Purpose:
Support scoring and quote preparation.

Questions:

1. Do you have an overall budget range for concierge support?
   - Under $600
   - $600-$1,500
   - $1,500-$3,000
   - $3,000-$7,500
   - $7,500-$15,000
   - $15,000+
   - Prefer to discuss privately
2. Are you ready to pay a planning deposit or booking deposit if availability matches your needs?
3. What payment method is preferred?
   - Payment link
   - Company card
   - Zelle
   - Revolut request
   - Invoice by approval
   - Discuss privately

Governance:
Do not collect card numbers through AI intake.

## 19. Phase 16: Privacy and Communication Preferences

Questions:

1. How should we handle your inquiry?
   - Standard coordination
   - Privacy-sensitive
   - Anonymous handling requested
   - Representative / assistant contact preferred
2. What is your preferred communication channel?
3. What time zone should we use for follow-up?
4. Is there anything that should not be included in written messages?

## 20. Phase 17: Final Review and Missing Details

AI should summarize:

- who the inquiry is for
- lane
- dates
- airport arrival/departure
- stay location
- matchday attendance
- obligations
- services requested
- security interest
- budget range
- privacy preference
- missing details
- next steps

AI should ask:

`Would you like to submit this for operator review and generate your Personal Matchday Command Hub Preview?`

## 21. Output Record

The intake should produce an operator-review record containing:

- inquiry ID
- lane
- access state
- privacy flag
- sensitive-status disclosure status
- service window
- trip dates
- arrival airport
- departure airport
- stay locations
- matchdays
- obligations
- requested services
- transportation needs
- food/beverage needs
- luggage needs
- security interest
- guest count
- budget range
- payment readiness
- missing fields
- recommended hub widgets
- operator review priority

## 22. Final Determination

The AI intake question bank is accepted as the operational question system for creating a Personal Matchday Command Hub Preview. It must guide the visitor through the full concierge discovery process while preserving privacy, security, operator confirmation, and claim boundaries.
