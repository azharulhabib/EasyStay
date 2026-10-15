'use server';
import { createCustomer, createOwner } from "@/libs/api";
import { redirect } from "next/navigation";
import { revalidatePath } from "next/cache";

function extractErrorMessage(response) {
  if (!response) return 'Registration failed. Please try again.';
  const err = response.errorData;
  if (!err) return response.statusText || 'Registration failed. Please try again.';

  if (typeof err === 'string') return err;
  if (err.error) return err.error;
  if (err.detail) return err.detail;
  if (err.email) return Array.isArray(err.email) ? err.email[0] : err.email;
  if (err.phone_number) return Array.isArray(err.phone_number) ? err.phone_number[0] : err.phone_number;
  if (err.password) return Array.isArray(err.password) ? err.password[0] : err.password;
  if (err.name) return Array.isArray(err.name) ? err.name[0] : err.name;
  if (err.non_field_errors) return Array.isArray(err.non_field_errors) ? err.non_field_errors[0] : err.non_field_errors;

  const firstKey = Object.keys(err)[0];
  if (firstKey && err[firstKey]) {
    const val = err[firstKey];
    return Array.isArray(val) ? `${firstKey}: ${val[0]}` : `${firstKey}: ${val}`;
  }

  return 'Registration failed or email already exists';
}

export async function signUpCustomerAction(prevState, formData) {
  
  if (formData.get('password') !== formData.get('confirmPassword')) {
    return { error: 'Passwords do not match' }
  };

  const userData = {
    email: formData.get('email'),
    name: formData.get('name'),
    phone_number: formData.get('phone'),
    password: formData.get('password'),
  };

  console.log(userData);

  try {
    const response = await createCustomer(userData);
    if (response?.status) {
      return { error: extractErrorMessage(response) };
    };
  } catch (error) {
    return { error: error.message || 'Registration failed. Please try again.' };
  };

  revalidatePath('/auth/login');
  redirect('/auth/login');
};

export async function signUpOwnerAction(prevState, formData) {
  if (formData.get('password') !== formData.get('confirmPassword')) {
    return { error: 'Passwords do not match' }
  };

  const userData = {
    email: formData.get('email'),
    name: formData.get('name'),
    phone_number: formData.get('phone'),
    password: formData.get('password'),
  };

  try {
    const response = await createOwner(userData);
    if (response?.status) {
      return { error: extractErrorMessage(response) };
    }
  } catch (error) {
    return { error: error.message || 'Registration failed. Please try again.' };
  };

  revalidatePath('/auth/login');
  redirect('/auth/login');
};