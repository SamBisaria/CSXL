/**
 * The Event Resolver allows the events to be injected into the routes
 * of components.
 *
 * @author Ajay Gandecha, Jade Keegan, Brianna Ta, Audrey Toney
 * @copyright 2023
 * @license MIT
 */

import { inject } from '@angular/core';
import { ResolveFn } from '@angular/router';
import { Event } from './event.model';
import { EventService } from './event.service';

/** This resolver injects the list of events into the events component. */
export const eventResolver: ResolveFn<Event[] | undefined> = (route, state) => {
  return inject(EventService).getEvents();
};

/** This resolver injects an event into the events detail component. */
export const eventDetailResolver: ResolveFn<Event | undefined> = (
  route,
  state
) => {
  console.log(route.paramMap);
  if (route.paramMap.get('id') != 'new') {
    return inject(EventService).getEvent(+route.paramMap.get('id')!);
  } else {
    return {
      id: null,
      name: '',
      time: new Date(),
      location: '',
      description: '',
      public: true,
      registration_limit: 0,
      organization_id: null,
      organization: null,
      registration_count: 0,
      is_attendee: false,
      is_organizer: false,
      organizers: []
    };
  }
};
