/**
 * This file was auto-generated by Fern from our API Definition.
 */
import express from "express";
import { CustomAuthService } from "./api/resources/customAuth/service/CustomAuthService";
export declare function register(expressApp: express.Express | express.Router, services: {
    customAuth: CustomAuthService;
}): void;